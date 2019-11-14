#define KBUILD_MODNAME "foo"
#include <uapi/linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_vlan.h>
#include <linux/ip.h>
#include <linux/ipv6.h>


//BPF_TABLE("percpu_array", uint32_t, long, dropcnt, 256);
BPF_ARRAY(hash_test, struct *,1); // Try to put a struct and pass it on the map

static inline int parse_ipv4(void *data, u64 nh_off, void *data_end) {
    struct iphdr *iph = data + nh_off;

    if ((void*)&iph[1] > data_end)
        return 0;
    return iph->protocol;
}

static inline int parse_ipv6(void *data, u64 nh_off, void *data_end) {
    struct ipv6hdr *ip6h = data + nh_off;

    if ((void*)&ip6h[1] > data_end)
        return 0;
    return ip6h->nexthdr;
}

struct parse_data {
	uint64_t num; // numbering for the data order
	unsigned char addr_0, addr_1, addr_2, addr_3, addr_4, addr_5; // allocate addresses
	
};

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
    u64 in2 = 2;
    u64 in3 = 3;
    u64 in4 = 4;
    u64 in5 = 5;
    struct parse_data dummy_data;
    struct iphdr *iph;

    struct eth_info {
        unsigned char addr[6];
    };

    nh_off = sizeof(*eth);

    if (data + nh_off  > data_end)
        return rc;

    h_proto = eth->h_proto;
    
    dummy_data = eth -> h_source[0];
  
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

// htons() converts the unsigned short integer hostshort from host byte order to network byte order
// host byte order can be little/big endian while network byte order is big endian
    if (h_proto == htons(ETH_P_IP)){
        index = parse_ipv4(data, nh_off, data_end);
        /*
        if (iph + 1 > data_end)
         {
         iph = data + nh_off;
         dummy_data = iph -> protocol;
         }
         */

        }
    else if (h_proto == htons(ETH_P_IPV6))
       index = parse_ipv6(data, nh_off, data_end);
    else
        index = 0;
    
 //   if (dummy_data0 == 144) {
    hash_test.update(&in0, &dummy_data);
//    }        

  //  value = dropcnt.lookup(&index);
 //   if (value)
 //       *value += 1;

    return rc;
}
