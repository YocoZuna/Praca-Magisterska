import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from scipy import signal as sp 
import os 
from scipy.fft import rfft, rfftfreq
import MovingAvrgFilter
from colormap import Colormap
from PIL import Image
MovingAvr = MovingAvrgFilter.Moving_Avgr_Filter()
buffor = []
elo = 0
NumberOfSDFT = 0

cm = Colormap()
my_cmap_red = cm.cmap_bicolor('black', 'red')
my_cmap_green = cm.cmap_bicolor('black', 'green')
my_cmap_blue = cm.cmap_bicolor('black', 'blue')

t = []
ax=[]
max = []
ay = []
az = []
x = []
y = []
z = []
pa = []
pb =[]
pc = []
def SDFT():

    window_length = 32;
    window = np.hamming(window_length);
    signal = ay
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);


    plt.figure(2);
    plt.title('Gy')
    figure_STFT_Gy = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_green);
    fig2 = plt.figure(2);
    fig2.canvas.draw()
    data2 = np.frombuffer(fig2.canvas.tostring_rgb(), dtype=np.uint8)
    data2 = data2.reshape(fig2.canvas.get_width_height()[::-1] + (3,))
    data2 = data2[58:428,80:577,:]

    signal = gz
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);

    plt.figure(3);
    plt.title('Gz')
    figure_STFT_Gz = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_blue);
    fig3 = plt.figure(3);
    fig3.canvas.draw()
    data3 = np.frombuffer(fig3.canvas.tostring_rgb(), dtype=np.uint8)
    data3 = data3.reshape(fig3.canvas.get_width_height()[::-1] + (3,))
    data3 = data3[58:428,80:577,:]

    im = plt.figure(3)
        
    signal = gx
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);

    plt.figure(4);
    plt.title('Gx')
    figure_STFT_Gx = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_red);
    fig4 = plt.figure(4);
    fig4.canvas.draw()
    data4 = np.frombuffer(fig4.canvas.tostring_rgb(), dtype=np.uint8)
    data4 = data4.reshape(fig4.canvas.get_width_height()[::-1] + (3,))
    data4 = data4[58:428,80:577,:]

    datargb = data2 + data3 + data4
    im = Image.fromarray(datargb)
    
    plt.savefig(f"C:\Temp\\{t[0]}.png")
    t.clear();ax.clear();max.clear();ax.clear();az.clear();x.clear();y.clear();z.clear();pa.clear();pb.clear();pc.clear()

def on_message(client, userdata, message):
    
    #file.writelines(str(message.payload)+"\n")
    # Ta czesc jest nie dokoczona 
    SDFTbuffor = str(message.payload[0:len(message.payload)-13])
    SplittedData = SDFTbuffor.split('),')
    for i in range(0,255):
        data = SplittedData[i]
        if i ==0:
            data=data[4:len(data)]
        else:
            data  = data[2:len(data)-1]
        sample,aax,aay,aaz,xx,yy,zz,phasea,phaseb,phasec = data.split(',')
        t.append(float(sample))
        ax.append(float(aax)-0.1044676)
        ay.append(float(aay)+0.0477295)
        az.append(float(aaz)-0.9561013)

        x.append(float(xx)+4.5992367)
        y.append(float(yy)+43.36626)
        z.append(float(zz)-1.5074805)
        
        pa.append(float(phasea))
        pb.append(float(phaseb))
        pc.append(float(phasec))
 
    SDFT()



mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("")
client.max_queued_messages_set(0)
client.connect(mqttBroker) 

client.loop_start()
while(1):

    client.subscribe("IMU")
    client.on_message=on_message 

    

client.loop_stop()