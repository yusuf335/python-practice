import paho.mqtt.client as paho  # mqtt library
import json
import time
import random

broker = "192.168.137.50"
topic = "esp/kdoj/ph";
port = 1883


def on_publish(client, userdata, result):
    print("published data is : ")
    pass


client1 = paho.Client("control1")
client1.on_publish = on_publish
client1.connect(broker, port, keepalive=60)

Count = 0

# publishing after every 5 secs
while True:

    Count += 1
    print(Count)
    data = {
            "Data-Received": Count,
            "turbidity": random.randint(0, 10),
            "ph": random.randint(0, 14),
            "temp": random.randint(0, 40),
            }

    ret = client1.publish(topic, payload=json.dumps(data))  # topic name is test
    print(data)
