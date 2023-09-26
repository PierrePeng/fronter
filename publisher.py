import time
import pandas as pd
import paho.mqtt.client as mqtt

if __name__ == '__main__':
    # Read data for local file
    data = pd.read_csv('sensor.csv')

    # Connect to MQTT
    client = mqtt.Client()
    client.connect("localhost", 1884)

    sample_hz = 6400

    # Publish data stream
    for value in data.iloc[:, 1]:
        client.publish("current", value, qos = 0)
        time.sleep(1/sample_hz)

    # Disconnect MQTT
    client.disconnect()
