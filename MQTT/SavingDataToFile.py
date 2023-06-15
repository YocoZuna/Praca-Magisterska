import paho.mqtt.client as mqtt
import time
file = open("TestMQTTServerS.txt","a+")
buffor = []
elo = 0
def on_message(client, userdata, message):
    
    file.writelines(str(message.payload)+"\n")

    

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("")
client.max_queued_messages_set(0)
client.connect(mqttBroker) 

client.loop_start()
while(1):

    client.subscribe("IMU")
    client.on_message=on_message 

    

client.loop_stop()