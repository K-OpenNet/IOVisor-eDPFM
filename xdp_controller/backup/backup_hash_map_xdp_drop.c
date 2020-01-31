#define KBUILD_MODNAME "foo"
#include <uapi/linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_vlan.h>
#include <linux/ip.h>
#include <linux/ipv6.h>

BPF_ARRAY(hash_addr, u64,2);
BPF_ARRAY(test_map, u64,2);
//BPF_HASH(hash_test, u64, u64, 10240 );	// -size default : 10240 but for test, I use 2
BPF_HASH(hash_test,u64, u64, 10240);

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
    return iph-> saddr;
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
    u64 ip_addr = 0;
    u64 *input_ip = 0;
    u64 test_ip =0;	// here, let's use the decimal instead of the octa (kernel form) 
    u64 zero = 0;
    u64 one = 1;
    u64 two = 2;
    u64 target_ip = 33663168;
//    u64 target_ip = 0;
    // 3232235778 = 192.168.1.2 or 33663168

    nh_off = sizeof(*eth);

    if (data + nh_off  > data_end)
        return rc;

    h_proto = eth->h_proto;
	
    hash_test.update(&target_ip, &zero);

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

    if (h_proto == htons(ETH_P_IP))
    {
        index = parse_ipv4(data, nh_off, data_end);
    	ip_addr = saddr_ipv4(data, nh_off, data_end);
    }
    else if (h_proto == htons(ETH_P_IPV6))
       index = parse_ipv6(data, nh_off, data_end);
    else
        index = 0;
    
    input_ip = hash_test.lookup(&ip_addr); // right now, compares the value of the key. Should change it to comparing the keys

    if (input_ip != NULL) // after looking up a value in the map, it must be tested if the return value isnt' NULL
    {
//	if (*input_ip == ip_addr)
		return XDP_DROP;	// drop packet
    }
//    return rc;
	return XDP_PASS;
}
