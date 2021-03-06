from kafka import KafkaConsumer
import sys
from ast import literal_eval
from pymongo import MongoClient
import pytz
#define information about kafka

bootstrap_servers = ['210.125.84.133:9092']
topicName = 'packetmonitor'

consumer = KafkaConsumer(topicName, bootstrap_servers = bootstrap_servers)

# database test - BEGIN

def insert_into_db(src_ip, pkt_num, time):
    client = MongoClient()
    db = client.packetmonitor    # database name
    collection = db.bpf2    # document name
    collection.insert_one({'src_ip':src_ip,'pkt_num':pkt_num,'time':time})
    
# database test - END

def kafka_consumer():
    print("kafka consumer test...")
    try :
        for message in consumer:
            value = message.value
            # value being saved appropriately has been confirmed
            # data is either parsed in 3 columns or 6 columns -> len : 30 && len : 60
#            print(value)
#            print('\n\n len : ')
#            print(value)
            length = len(value)
#                src_ip = decimal_to_human(str(value[i*22:(i+1)*22-11]))   # first ten digits parsed
#                dst_ip = decimal_to_human(str(value[(i+1)*22-11:(i+1)*22]))  # second ten digits parsed
#                insert_into_db(src_ip, dst_ip, '111')
            counter = 0
            for i in value[::-1]: # to find time in the string, reverse the string for iterated lookup
                if i == ' ':
                    break
                else:
                    counter = counter + 1

#            print('source ip ' + str(value[:10]) + 'num : ' + str(value[11:-counter])) + 'time : ' + str(value[-counter:])
            source_ip = decimal_to_human(str(value[:10]))
            pkt_num = str(value[11:-counter])
            time = str(value[-counter:])
            print('source ip : ' + source_ip + 'packet : ' + pkt_num) + 'time : ' + str(value[-counter:])
            insert_into_db(source_ip, pkt_num, time)
            '''
            if (len(value) == 30):
#                print(value)
                src_ip_0 = str(decimal_to_human(str(value[9:19])))
                dst_ip_0 = str(decimal_to_human(str(value[20:30])))
                print(' src1 : ' + str(src_ip_0) + 'dst1 : ' + str(dst_ip_0))
                time_temp = '111'
                insert_into_db(src_ip_0,dst_ip_0,time_temp)
                
            elif (len(value) == 60):
#                print(value)
                time_temp = '111'
                src_ip_0 = str(decimal_to_human(str(value[9:19])))
                dst_ip_0 = str(decimal_to_human(str(value[20:30])))
                src_ip_1 = str(decimal_to_human(str(value[39:49])))
                dst_ip_1 = str(decimal_to_human(str(value[50:60])))
                print(' src1 : ' + str(src_ip_0) + ' dst1 : ' + str(dst_ip_0) + ' src2 : '+ str(src_ip_1) + ' dst2 : ' + str(dst_ip_1))
                insert_into_db(src_ip_0,dst_ip_0,time_temp)
                insert_into_db(src_ip_1,dst_ip_1,time_temp)
            '''
    except KeyboardInterrupt:
        sys.exit()

def decimal_to_human(input_value):
    input_value = int(input_value)
    hex_value = hex(input_value)[2:]
    pt3 = literal_eval((str('0x'+str(hex_value[-2:]))))
    pt2 = literal_eval((str('0x'+str(hex_value[-4:-2]))))
    pt1 = literal_eval((str('0x'+str(hex_value[-6:-4]))))
    pt0 = literal_eval((str('0x'+str(hex_value[-8:-6]))))
    result = str(pt0)+'.'+str(pt1)+'.'+str(pt2)+'.'+str(pt3)
    return result


kafka_consumer()

