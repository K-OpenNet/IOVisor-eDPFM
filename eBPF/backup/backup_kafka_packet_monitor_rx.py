from kafka import KafkaConsumer
import sys
from ast import literal_eval

#define information about kafka

bootstrap_servers = ['localhost:9092']
topicName = 'packetmonitor'

consumer = KafkaConsumer(topicName, bootstrap_servers = bootstrap_servers)

def kafka_consumer():
    print("kafka consumer test...")
    try :
        for message in consumer:
            value = message.value
            if (value[0] != '0'):
                if (value != '9999999'):
                    value = str(value)
                    print(decimal_to_human(value))
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
