#!/usr/bin/python
#
# xdp_drop_count.py Drop incoming packets on XDP layer and count for which
#                   protocol type
#
# Copyright (c) 2016 PLUMgrid
# Copyright (c) 2016 Jan Ruth
# Licensed under the Apache License, Version 2.0 (the "License")
from bcc import BPF
import pyroute2
import time
import sys
#from ctypes import *
import ctypes
import json

def convert_ip_to_bin(primal):  # converts human friendly addr to machine friendly addr
    marker = primal.find('.')
    one = int(primal[0:primal.find('.')])
    primal = primal[marker+1:]
    marker = primal.find('.')
    two = int(primal[0:marker])
    primal = primal[marker+1:]
    marker = primal.find('.')
    three = int(primal[0:marker])
    primal = primal[marker+1:]
    four = int(primal[0:])
    primal = primal[marker+1:]
    one = "{0:b}".format(one).zfill(8)
    two = "{0:b}".format(two).zfill(8)
    three = "{0:b}".format(three).zfill(8)
    four = "{0:b}".format(four).zfill(4)
    seq = (four, three, two, one)
    result = ''.join(seq)
    #result = ''.join(one)
    return result

def convert_bin_to_ip(data): # converts machine friendly addr to human firneldy addr
    data =  "{0:b}".format(data.value).zfill(28)
#    data = ''.join(str((int((data[0:4]),2))))
# 0:4 - 1
# 4:12 - 1
# 12:20 - 168
# 20:28
    
    one = ''.join(str((int((data[20:28]),2))))
    two = ''.join(str((int((data[12:20]),2))))
    three = ''.join(str((int((data[4:12]),2))))
    four = ''.join(str((int((data[0:4]),2))))
    back = one +'.' + two + '.'+ three +'.' + four
    return back

flags = 0
def usage():
    print("Usage: {0} [-S] <ifdev>".format(sys.argv[0]))
    print("       -S: use skb mode\n")
    print("e.g.: {0} eth0\n".format(sys.argv[0]))
    exit(1)

if len(sys.argv) < 2 or len(sys.argv) > 3:
    usage()

if len(sys.argv) == 2:
    device = sys.argv[1]

XDP_FLAGS_SKB_MODE = 1 << 1
XDP_FLAGS_DRV_MODE = 1 << 2
XDP_FLAGS_HW_MODE = 1 << 3

if len(sys.argv) == 3:
    if "-S" in sys.argv:
        # XDP_FLAGS_SKB_MODE
        flags |= 1 << 1

#listeners = PLAINTEXT://210.125.84.133:9092

    if "-S" == sys.argv[1]:
        device = sys.argv[2]
    else:
        device = sys.argv[1]

mode = BPF.XDP
#mode = BPF.SCHED_CLS

if mode == BPF.XDP:
    ret = "XDP_PASS"
    ctxtype = "xdp_md"
else:
    ret = "TC_ACT_SHOT"
    ctxtype = "__sk_buff"

_xdp_file = "my_xdp.c"
# load BPF program
b = BPF(src_file=_xdp_file, cflags=["-w", "-DRETURNCODE=%s" % ret, "-DCTXTYPE=%s" % ctxtype])

fn = b.load_func("xdp_prog1", mode)


if mode == BPF.XDP:
    b.attach_xdp(device, fn, flags)
#    b.attach_xdp(device, fn, flags)
else:
    ip = pyroute2.IPRoute()
    ipdb = pyroute2.IPDB(nl=ip)
    idx = ipdb.interfaces[device].index
    ip.tc("add", "clsact", idx)
    ip.tc("add-filter", "bpf", idx, ":1", fd=fn.fd, name=fn.name,
          parent="ffff:fff2", classid=1, direct_action=True)

hash_test = b.get_table("hash_test")
in_test = 3;
tester = 13
prev = [0] * 256

print("Printing drops per IP protocol-number, hit CTRL+C to stop")
while 1:
    print("primal hunt")
    try:
        print(hash_test.items())
        data = (hash_test.items()[0][1])
        print('\n')
        print("data : ")
        print(data)

        time.sleep(1)
    except KeyboardInterrupt:
        print("Removing filter from device")
        break;

if mode == BPF.XDP:
    b.remove_xdp(device, flags)
else:
    ip.tc("del", "clsact", idx)
    ipdb.release()