import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import serial
import struct
mqttBroker ="mqtt.eclipseprojects.io" 
vals = []
sample  = []
iterrator = 1
dataBuffor = []
bufforSize = 10280
unpackedData = []
for i in range(0,int(bufforSize/40)):
    
    sample.append(iterrator)
    iterrator += 40
stm32 = serial.Serial(baudrate=921600,port="COM3")
client = mqtt.Client("IMU")
client.connect(mqttBroker) 
client.max_queued_messages_set(0)
dataa = []
print("Initlizing....")
time.sleep(5)
stm32.write('s'.encode('ascii'))

while True:
    startcond = stm32.read(1)
    if (startcond == b'S'):
        dataa = stm32.read_until(b'END')

        data = dataa[0:len(dataa)-3]
 
        for i in range(0,255):
        
            dataBuffor = data[sample[i]:sample[(i+1)]]
            tempVal = dataBuffor[0:len(dataBuffor)]
            try:
                unpackedData.append(struct.unpack('<ifffffffff',tempVal))
            except:
                continue
            dummy = 0
        unpackedData.append("\n")
        client.publish("IMU", str(unpackedData))
        unpackedData.clear()
                
        

            



