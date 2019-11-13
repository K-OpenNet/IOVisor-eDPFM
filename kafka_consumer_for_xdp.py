from kafka import KafkaConsumer
import sys

bootstrap_servers = ['localhost:9091','localhost:9092','localhost:9090']
topicName = 'xdp_kafka_topic'

consumer = KafkaConsumer (topicName, group_id = 'group1', bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')

try:
    for message in consumer:
#        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
        value = message.value
        print(value)

except KeyboardInterrupt:
    sys.exit()
