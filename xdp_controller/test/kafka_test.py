from kafka import KafkaConsumer

bootstrap_servers = ['210.117.251.25'] # k-post
topicName = 'bpf2'

consumer = KafkaConsumer(topicName, bootstrap_servers = bootstrap_servers)

def kafka_consumer():
    print('kafka consumer...')
    try:
        for message in consumer:
            print(message.value)
    except KeyboardInterrupt:
        sys.exit()


kafka_consumer()
