import paho.mqtt.client as mqtt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from scipy import signal as sp 
import math
import os 
from scipy.fft import rfft, rfftfreq
buffor = []
iterator = 0
def on_message(client, userdata, message):
  
    line = str(message.payload.decode("utf-8"))
    line = line[2:-4]
    sample,aax,aay,aaz,xx,yy,zz = line.split(';')

    t.append(float(sample))
    ax.append(float(aax)-0.1044676)
    ay.append(float(aay)+0.0477295)
    az.append(float(aaz)-0.9561013)

    gx.append(float(xx)+4.5992367)
    gy.append(float(yy)+43.36626)
    gz.append(float(zz)-1.5074805)
    axyfft = rfft(ax)
    axfft = rfftfreq(len(ax), 1/500)

    ayyfft = rfft(ay)
    ayfft = rfftfreq(len(ay), 1/500)

    azyfft = rfft(az)
    azfft = rfftfreq(len(az), 1/500)


    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    #plt.axis('off')
    plt.title("Acc")
    #plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    #plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
 
    plt.savefig(f"{iterator}.png")

mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("fft_sdft")
client.connect(mqttBroker) 
t = []
ax=[]
ay = []
az = []
gx = []
gy = []
gz = []


client.loop_start()

while 1:

    client.subscribe("IMU")
    client.on_message=on_message


client.loop_stop()