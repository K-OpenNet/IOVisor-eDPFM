from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092','localhost:9091','localhost:9090']
topicName = 'xdp_kafka_topic'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
content = "test works"
#ack = producer.send(topicName, b'Hello World!!!!!')
# in the code above, figure out what 'b' is for in b'Hello World!!!!!' 
ack = producer.send(topicName, content)

metadata = ack.get()
print(metadata.topic)
print(metadata.partition)

producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5, value_serializer=lambda m: json.dumps(m).encode('ascii'))
