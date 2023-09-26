import paho.mqtt.client as mqtt
import time

# Callback function for connect
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #Subscribe for special topic name
    client.subscribe("current")

# Callback function for recevie message
def on_message(client, userdata, msg):
    print("Received message: ", msg.payload.decode())

client = mqtt.Client()

# Bundle callback event
client.on_connect = on_connect
client.on_message = on_message

# Connect MQTT
client.connect("localhost", 1884)

client.loop_forever()
