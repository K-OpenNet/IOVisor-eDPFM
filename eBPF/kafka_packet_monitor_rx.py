from kafka import KafkaConsumer
import sys

#define information about kafka

bootstrap_servers = ['localhost:9092']
topicName = 'packetmonitor'

consumer = KafkaConsumer(topicName, group_id = 'group1', bootsrap_servers = bootstrap_servers)

def kafka_consumer():
    print("kafka consumer test...")
    try :
        for message in consumer:
            value = message.value
            if (value[0] != '0'):
                print(value)
                print('\n')
    except KeyboardInterrupt:
        sys.exit()


