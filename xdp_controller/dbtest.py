from pymongo import MongoClient
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import subprocess

producer = KafkaProducer(bootstrap_servers=['localhost:9093'])
topicName = 'controller'

client = MongoClient()
client = MongoClient('localhost',27017)
db = client['packetmonitor']
collection = db['bfp2']

time_test = time.localtime()

THRESHOLD = 110
shit = str('141414')

#find specfic value :
# db.bpf2.find({"time":"2020;2;16;7;28;2"})

# can query for data that have time less than '2020;2;16;7;28;1' by using :
# db.bpf2.find({'time':{ $lt: '2020;2;16;7;28;1'}})
# can query for data that have time less than '2020;2;16;7;28;1', greater than '2020;2;16;7;27;57' by using:
# db.bpf2.find({'time':{ $lt:'2020;2;16;7;28;1', $gt:'2020;2;16;7;27;57'}})

# below works

#for value in db.bpf2.find({'time':{ '$lt':'2020;2;16;7;28;1', '$gt':'2020;2;16;7;27;57'}}):
#    print(value)

current_time = str(time.localtime()[0])+';'+str(time.localtime()[1])+';'+str(time.localtime()[2])+';'+str(time.localtime()[3])+';'+str(time.localtime()[4])+';'+str(time.localtime()[5])

print('current time : ' + str(current_time))

xdp_status = 0  # mark xdp status

while(1):
    tot_pkt = 0
    counter = 0
    for value in db.bpf2.find({'time':{ '$lt':'2020;2;16;7;28;2', '$gt':'2020;2;16;7;27;57'}},{'pkt_num':1,'_id':0}): # lt boundary is not includeda
        time.sleep(1)
        tot_pkt = tot_pkt + int(str(value)[15:-2])
    if (tot_pkt > THRESHOLD and xdp_status == 0):   # if total packet exceeds the threshold and xdp_status is turned off, turn it on
        while(counter < 100):
    #        producer.send(topicName,'192 168 000 002 a')
            producer.send(topicName,'192 168 000 002 a')
            counter = counter + 1
    elif (tot_pkt < THRESHOLD and xdp_status ==1):
        while(counter < 100):
            producer.send(topicName,'192 168 000 002 d')
            counter = counter + 1
    print('total pkt : ' +  str(tot_pkt))


# after connecting producer.send(), all I have to to do is make XDP controller receive the msg and turn on xdp 


