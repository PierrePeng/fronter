# Prerequired

1. Install python package   
    >pip3 install pandas paho-mqtt

2. linux package mqtt
    >sudo apt-get install mosquitto
# Run

1. Run MQTT server in terminal
    >mosquitto -p 1884

2. Run subcriber
   > python3 subscriber.py

3. Run publisher
   > python3 publisher.py
