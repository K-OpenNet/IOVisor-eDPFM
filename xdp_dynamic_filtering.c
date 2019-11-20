#define KBUILD_MODNAME "foo"
#include <uapi/linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_vlan.h>
#include <linux/ip.h>
#include <linux/ipv6.h>

BPF_TABLE(MAPTYPE, uint32_t, long, pktcnt, 256);
BPF_ARRAY(hash_addr, u64,12);

static inline int parse_ipv4(void *data, u64 nh_off, void *data_end) {
    struct iphdr *iph = data + nh_off;

    if ((void*)&iph[1] > data_end)
        return 0;
    return iph->protocol;
}

static inline int saddr_ipv4(void *data, u64 nh_off, void *data_end) {
    struct iphdr *iph = data + nh_off;

    if ((void*)&iph[1] > data_end)
	return 0;
    return iph -> saddr;
}


static inline int parse_ipv6(void *data, u64 nh_off, void *data_end) {
    struct ipv6hdr *ip6h = data + nh_off;

    if ((void*)&ip6h[1] > data_end)
        return 0;
    return ip6h->nexthdr;
}

int xdp_prog1(struct CTXTYPE *ctx) {

    void* data_end = (void*)(long)ctx->data_end;
    void* data = (void*)(long)ctx->data;

    struct ethhdr *eth = data;

    // drop packets
    int rc = RETURNCODE; // let pass XDP_PASS or redirect to tx via XDP_TX
    long *value;
    uint16_t h_proto;
    uint64_t nh_off = 0;
    uint32_t index;
    u64 in0 = 0;
    u64 in1 = 1;
    u64 ip_addr0 = 0;
    u64 ip_addr1 = 0;
    u64 addr_cnt = 0; // address counter to count how many addresses have been accounted for
    u64 temp = 0;
    nh_off = sizeof(*eth);

    if (data + nh_off  > data_end)
        return rc;

    h_proto = eth->h_proto;

    // parse double vlans
    #pragma unroll
    for (int i=0; i<2; i++) {
        if (h_proto == htons(ETH_P_8021Q) || h_proto == htons(ETH_P_8021AD)) {
            struct vlan_hdr *vhdr;

            vhdr = data + nh_off;
            nh_off += sizeof(struct vlan_hdr);
            if (data + nh_off > data_end)
                return rc;
                h_proto = vhdr->h_vlan_encapsulated_proto;
        }
    }

u64   temp_addr = saddr_ipv4(data,nh_off, data_end);

    if (h_proto == htons(ETH_P_IP))
    {
	if ( hash_addr.lookup(&in0) == 
        index = parse_ipv4(data, nh_off, data_end);
	// this is where I can save the IP addrsses : WORK HERE .. look up the map and decide which counter to increment
	hash_addr.update(&in0, &temp_addr);
    }
    else if (h_proto == htons(ETH_P_IPV6))
       index = parse_ipv6(data, nh_off, data_end);
    else
       index = 0;

    // Now the addresses have been added to BPF maps
    // Now I will try to leverage maps and try to distinguish packets according to them



    value = pktcnt.lookup(&index);	// use lookup to get the value

    if (value)
        __sync_fetch_and_add(value, 1);

    return rc;
}
