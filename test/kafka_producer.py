from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
bootstrap_servers = ['localhost:9092']
topicName = 'test'

data = 'vini veri vidi vici'

producer = KafkaProducer(bootstrap_severs=['localhost:9092'], value_serializer=lambda x: 
        dumps(x).encode('utf-8'))
producer.send('test',data)
