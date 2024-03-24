import pulsar
from streamz import Stream


# client = pulsar.Client('pulsar://localhost:6650')
# consumer = client.subscribe('my-topic', subscription_name='my-sub')

s = Stream.from_pulsar(['my-output'],
                       subscription_name='my-sub',
                       consumer_params={
                           'service_url':
                               'pulsar://localhost:6650'})

s.map(lambda x: x.decode())
L = s.sink_to_list()

s.start()
while True:
    try:
        # msg = consumer.receive()
        # print("Received message: '%s'" % msg.data())
        # consumer.acknowledge(msg)
        if L:
            print(L.pop(0))
    except pulsar.Interrupted:
        print("Stop receiving messages")
        break

# client.close()
