import paho.mqtt.client as mqtt
import random
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))


# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("yusuf", "Yusuf@10335")

# connect to HiveMQ Cloud on port 8883
client.connect("be6241994b9d49b1a3f661ada2f376a0.s1.eu.hivemq.cloud", 8883)

Count = 0
topic = "saj/sensor/pc";

while True:

    Count += 1
    print(Count)
    data = {
        "Data-Received": Count,
        "turbidity": random.randint(0, 10),
        "ph": random.randint(0, 14),
        "temp": random.randint(0, 40),
    }

    client.publish(topic, payload=json.dumps(data))