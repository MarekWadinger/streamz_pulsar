from streamz import Stream


# client = pulsar.Client('pulsar://localhost:6650')
# producer = client.create_producer('my-topic')

source = Stream()
producer_ = source.to_pulsar(
    'my-topic', producer_config={
        'service_url': 'pulsar://localhost:6650'})

for i in range(3):
    # producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
    source.emit(('hello-pulsar-%d' % i).encode('utf-8'))

# client.close()
producer_.stop()
producer_.flush()
