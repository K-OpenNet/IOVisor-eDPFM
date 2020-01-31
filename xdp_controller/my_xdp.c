#define KBUILD_MODNAME "foo"
#include <uapi/linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_vlan.h>
#include <linux/ip.h>
#include <linux/ipv6.h>

//BPF_TABLE("percpu_array", uint32_t, long, dropcnt, 256);
BPF_ARRAY(hash_test, u64,3);
BPF_ARRAY(black_list, u64,3);

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
    u64 in_0 = 0;
    u64 in_1 = 1;
    u64 in0 = 0;
    u64 in1 = 1;
    u64 in2 = 2;
    u64 *input_test=0;
//    u64 in2 = 2;
//    u64 in3 = 3;
//    u64 in4 = 4;
//    u64 in5 = 5;
    u64 dummy_data1, dummy_data2, dummy_data3, dummy_data4, dummy_data5, dummy_data0;
	
    struct iphdr *iph;

    struct eth_info {
        unsigned char addr[6];
    };

    nh_off = sizeof(*eth);

    if (data + nh_off  > data_end)
        return rc;

    h_proto = eth->h_proto;

    /*
     *
     * CODE BELOW RETRIEVES the ethernet address
     * 
    dummy_data0 = eth -> h_source[0];
    dummy_data1 = eth -> h_source[1];
    dummy_data2 = eth -> h_source[2];
    dummy_data3 = eth -> h_source[3];
    dummy_data4 = eth -> h_source[4];
    dummy_data5 = eth -> h_source[5];

    dummy_data0 = eth -> h_dest[0];
    dummy_data1 = eth -> h_dest[1];
    dummy_data2 = eth -> h_dest[2];
    dummy_data3 = eth -> h_dest[3];
    dummy_data4 = eth -> h_dest[4];
    dummy_data5 = eth -> h_dest[5];
  */  

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


    if (h_proto == htons(ETH_P_IP)){
        index = parse_ipv4(data, nh_off, data_end);
        }
    else if (h_proto == htons(ETH_P_IPV6))
       index = parse_ipv6(data, nh_off, data_end);
    else
        index = 0;

	u64 binary[32];
	int i=0;
	for (i=0; i<32; i++)
		binary[i] = 0;
      dummy_data0 = 99;   
      dummy_data1 = 98;
      hash_test.update(&in0, &dummy_data0);
      hash_test.update(&in1, &dummy_data1);
      input_test = hash_test.lookup(&in0);
      hash_test.update(&in2, &dummy_data1);
      if (input_test != NULL)
	      black_list.update(&in2, input_test);
    
    if (dummy_data0 = 33663168)	// BLOCK AN IP HERE
	    return XDP_PASS; // TO BLOCK, CHANGE THIS CODE TO XDP_DROP;


    return rc;
}
