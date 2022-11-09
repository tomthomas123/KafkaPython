import time
from kafka import KafkaProducer
bootstrap_server = ["localhost:9092"]
topic = "nestDigital"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)
producer = KafkaProducer()
data = "Hello consumer"
def senddata():
    message = producer.send(topic,bytes(data,"utf-8"))
    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)

while True:
    senddata()
