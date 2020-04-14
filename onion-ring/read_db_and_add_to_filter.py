import os
import subprocess
from pymongo import MongoClient
import time

IP_EDGEBOX1 = '172.30.84.93'
IP_EDGEBOX2 = '172.30.84.92'
IP_KUBE1 = '172.30.84.95'
IP_KUBE2 = '172.30.84.94'
IP_MASTER = '172.30.84.96'

# connecting to pymongo db

PKT_THRESHOLD = 10

client = MongoClient('localhost',27017)
db = client['packetmonitor']
collection = db['bpf2']

result = 0

def print_value():
    current_time = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]).zfill(2)

    current_time_minus_5 = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]-5).zfill(2)
    global result
 
    for post in collection.find({'time':{'$gt':current_time_minus_5,'$lt':current_time}},{'_id':0,'dst_ip':1,'pkt_num':1}):
        num_edgebox1 = 0
        num_edgebox2 = 0
        num_kube1 = 0
        num_kube2 = 0
        num_master = 0
        print(post)
        temp_ip = str(post)[14:26]
        print('temp ip ' + temp_ip)
        counter = 0
        temp = str(post)[::-1]
        for i in temp:
            if i == ':':
                break
            else:
                counter = counter+1

        temp_pkt_num = str(post)[-counter+3:-2]
        print('temp_pkt_num : ' + str(temp_pkt_num))
        print(post)

        
    

#        print(post)
#        result = result + int(str(post)[15:-2])

# to write a system command, refer to the line below:
#subprocess.call(["apt-get","update"])
#subprocess.checkoutput(

# remove the annotation block and integratre this code later 
# save black_list map id - begin
'''
num = entire_bpf_map_info.find("black_list")
test = num - 30
test2 = entire_bpf_map_info[test:num]
num2 = test2.find('\n')
test3 = test2[num2:]
num3 = test3.find(':')
test4 = test3[:num3]
black_list_map_id = int(test4)
print('- targetted bpf map id : ' + str(test4))
'''
#save black_list map id - end

# update bpf map value - begin
#subprocess.call(["bpftool","map","update","id",str(black_list_map_id),"key","00","00","00","00","value","01","00","00","00","00","00","00","00"])
# update bpf map value - end


ip_address = []
pkt_num = []

def add_to_ip_saver(addr_merged, num):
    global ip_address
    global pkt_num

    if (addr_merged in ip_address):        # when returns True
        index = ip_address.index(addr_merged)
        pkt_num[index] = str(int(pkt_num[index]) + int(num))
    elif (not addr_merged in ip_address):  # when returns False
        ip_address.append(addr_merged)
        pkt_num.append(num)

def search_db():
    print('search db init')
    global ip_address
    global pkt_num
    current_time = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]).zfill(2)

    current_time_minus_5 = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]-4).zfill(2)
    for value in collection.find({'time':{'$gt':current_time_minus_5,'$lt':current_time}},{'src_ip':1,'dst_ip':1,'_id':0,'pkt_num':1}):
        print(current_time)
        print(current_time_minus_5)
        src_ip = str(value)[14:25]
        dst_ip = str(value)[41:52]
        addr_merged = src_ip + '/' + dst_ip
        num = str(value)[69:-3]
        add_to_ip_saver(addr_merged, num)


try:
    while True:
        print_value()
        time.sleep(4)
except KeyboardInterrupt:
    pass
