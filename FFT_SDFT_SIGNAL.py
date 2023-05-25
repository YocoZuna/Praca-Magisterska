import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from scipy import signal as sp 
import math
import os 
from scipy.fft import rfft, rfftfreq
import MovingAvrgFilter
MovingAvr = MovingAvrgFilter.Moving_Avgr_Filter()
count = 0
#importing data set
#dataset = open("test.csv",'r').read()
first_sample = 1280
lista = [ ]
listsize = 0
PathToFile = "Run_With_Broke_Prop\\ReadImu.csv"
#PathToFile = "ReadImu.csv"

dataset = open(PathToFile,'r').readlines()   
temp = 0
for i in dataset:
    if i == '\n':
        dataset.remove('\n')
print(len(dataset))
try:
 
    listsize = len(dataset)
    print(listsize)
except:
    print("Could not open CSV file\n")

for i in range(0,(int(listsize/256))):
    
    lista.append(temp)
    temp = temp +256


lenth = len(lista)
iterration= 0
while iterration <= lenth:
    try:
       
        temp1 = lista[iterration]
        temp2 = lista[iterration+1]
        datasett = dataset[temp1:temp2]
    except:
        break
    
    #lines = dataset.split("\n")
    iterration+=1
    lines = datasett
    
    t = []
    ax=[]
    ay = []
    az = []
    gx = []
    gy = []
    gz = []



    for line in lines:
        if len(line) > 1:
            
            sample,aax,aay,aaz,xx,yy,zz = line.split(',')
            t.append(float(sample))
            ax.append(float(aax)-0.1044676)
            ay.append(float(aay)+0.0477295)
            az.append(float(aaz)-0.9561013)

            gx.append(float(xx)+4.5992367)
            gy.append(float(yy)+43.36626)
            gz.append(float(zz)-1.5074805)


            



            """FFT"""
            
       
    axyfft = rfft(gx)
    axfft = rfftfreq(len(gx), 1/400)

    ayyfft = rfft(gy)
    ayfft = rfftfreq(len(gy), 1/400)

    azyfft = rfft(gz)
    azfft = rfftfreq(len(gz), 1/400)
   
    """    fft = [ax,ay,az] 


    axyfft = rfft(fft[0])
    axfft = rfftfreq(len(fft[0]), 1/200)

    ayyfft = rfft(fft[1])
    ayfft = rfftfreq(len(fft[1]), 1/200)

    azyfft = rfft(fft[2])
    azfft = rfftfreq(len(fft[2]), 1/200)
    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    plt.title("Acc")
    plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
    plt.savefig(f"Smietnik\\Acc_FFT{count}.png")
    plt.figure(1).clear()
    count = count+1"""

    print(f" Time_Start {t[0]}\n Time_End {t[-1]}\n")
    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    #plt.axis('off')
    plt.title("Acc")
    #plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    #plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
 
    #plt.savefig("Dupal.png")
    """SDFT"""

    window_length = 256;
    window = np.hamming(window_length);
    signal = gy
    fs = 200


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);


    plt.figure(2);
    plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest');
    
    plt.ylabel('Frequency (Hz)');
    plt.xlabel('Time (s)');
    plt.show()
    plt.figure(1).clear()
    plt.figure(2).clear()