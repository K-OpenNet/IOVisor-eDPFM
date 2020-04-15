import os
import subprocess
from pymongo import MongoClient
import time

IP_EDGEBOX1 = '172.30.84.93'
IP_EDGEBOX2 = '172.30.84.92'
IP_KUBE1 = '172.30.84.95'
IP_KUBE2 = '172.30.84.94'
IP_MASTER = '172.30.84.96'
IP_EDGEBOX2_VM1 = '192.168.122.205'
IP_EDGEBOX2_VM2 = '192.168.122.134'
IP_EDGEBOX2_VM3 = '192.168.122.142'
IP_EDGEBOX1_VM1 = '192.168.122.178'
IP_EDGEBOX1_VM2 = '192.168.122.173'

# connecting to pymongo db

PKT_THRESHOLD = 10

client = MongoClient('localhost',27017)
db = client['packetmonitor']
collection = db['bpf2']

result = 0

def print_value():
        num_edgebox1 = 0
        num_edgebox2 = 0
        num_kube1 = 0
        num_kube2 = 0
        num_master = 0
        num_edgebox2_vm1 = 0
        num_edgebox2_vm2 = 0
        num_edgebox2_vm3 = 0
        num_edgebox1_vm1 = 0
        num_edgebox1_vm2 = 0

        current_time = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]).zfill(2)

        current_time_minus_5 = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]-5).zfill(2)
        global result
 
        for post in collection.find({'time':{'$gt':current_time_minus_5,'$lt':current_time}},{'_id':0,'dst_ip':1,'pkt_num':1}):
            print(post)
            pos_start = str(post).find('u\'dst_ip\': ') + 13
            pos_end = str(post).find(', u\'pkt_num\':') -1
            temp_ip = str(post)[pos_start:pos_end]

            counter = 0
            temp = str(post)[::-1]
            for i in temp:
                if i == ':':
                    break
                else:
                    counter = counter+1

            temp_pkt_num = int(str(post)[-counter+3:-2])
            print(temp_ip)
            if (temp_ip == IP_EDGEBOX1):
                num_edgebox1 = num_edgebox1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2):
                num_edgebox2 = num_edgebox2 + temp_pkt_num
            elif (temp_ip == IP_KUBE1):
                num_kube1 = num_kube1 + temp_pkt_num
            elif (temp_ip == IP_KUBE2):
                num_kube2 = num_kube2 + temp_pkt_num
            elif (temp_ip == IP_MASTER):
                num_master = num_master + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM1):
                num_edgebox2_vm1 = num_edgebox2_vm1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM2):
                num_edgebox2_vm2 = num_edgebox2_vm2 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM3):
                num_edgebox2_vm3 = num_edgebox2_vm3 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX1_VM1):
                num_edgebox1_vm1 = num_edgebox1_vm1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX1_VM2):
                num_edgebox1_vm2 = num_edgebox1_vm2 + temp_pkt_num

        print("edgebox1 " + str(num_edgebox1))
        print("edgebox2 " + str(num_edgebox2))
        print("kube1 " + str(num_kube1))
        print("kube2 " + str(num_kube2))
        print("master " + str(num_master))
        print("edgebox2_vm1 " + str(num_edgebox2_vm1))
        print("edgebox2_vm2 " + str(num_edgebox2_vm2))
        print("edgebox2_vm3 " + str(num_edgebox2_vm3))
        print("edgebox1_vm1 " + str(num_edgebox1_vm1))
        print("edgebox1_vm2 " + str(num_edgebox1_vm2))

        f = open('edgebox1.txt','w')
        f.write(str(num_edgebox1))
        f.close()
        f = open('edgebox2.txt','w')
        f.write(str(num_edgebox2))
        f.close()
        f=open('kube1.txt','w')
        f.write(str(num_kube1))
        f.close()
        f=open('kube2.txt','w')
        f.write(str(num_kube2))
        f.close()
        f=open('master.txt','w')
        f.write(str(num_master))
        f.close()
        f=open('edgebox2_vm1.txt','w')
        f.write(str(num_edgebox2_vm1))
        f.close()
        f=open('edgebox2_vm2.txt','w')
        f.write(str(num_edgebox2_vm2))
        f.close()
        f=open('edgebox2_vm3.txt','w')
        f.write(str(num_edgebox2_vm3))
        f.close()
        f=open('edgebox1_vm1.txt','w')
        f.write(str(num_edgebox1_vm1))
        f.close()
        f=open('edgebox1_vm2.txt','w')
        f.write(str(num_edgebox1_vm2))
        f.close()

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
        time.sleep(1)
except KeyboardInterrupt:
    pass
