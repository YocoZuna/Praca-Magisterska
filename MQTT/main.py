from STEval import ST_EVal
from STMF411RE import ST_F411
import paho.mqtt.client as mqtt
import time
buffor = []

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("main")
client.connect(mqttBroker) 


client.loop_start()
while 1:
    client.subscribe("IMU")
    client.on_message=on_message 


client.loop_stop()


