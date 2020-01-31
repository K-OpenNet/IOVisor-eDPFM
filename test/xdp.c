#include <linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_vlan.h>
#include <linux/ip.h>
#include <linux/ipv6.h>

//BPF_ARRAY(test_map, u64, 2);

struct bfp_map_def SEC("maps") my_map = {
	.type = BPF_MAP_TYPE_HASH,
	.key_size = sizeof(int),
	.value_size = sizeof(int),
	.max_entries = 100,
	.map_flags = BPF_F_NO_PREALLOC,
};

int main()
{
	BPF_ARRAY(test_map, u64, 2);

	return XDP_DROP;
}
