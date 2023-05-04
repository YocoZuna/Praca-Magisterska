import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import math
from scipy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2 as cv
from scipy import signal as sp 
#importing data set
#dataset = open("test.csv",'r').read()
first_sample = 1280
lista = [ ]
listsize = 0
t = []
ax=[]
ay = []
az = []
x = []
y = []
z = []
PathToFile = "Run_With_Broke_Prop\\ReadImu.csv"
try:
    dataset = open(PathToFile,'r').readlines()
    listsize = len(dataset)
    print(listsize)
except:
    print("Could not open CSV file\n")
    
temp = 0
for i in range(0,(int(listsize/128))):
    
    lista.append(temp)
    temp = temp +128

i = 0


lenth = len(lista)
iterration= 0
while iterration <= lenth:
    try:
        dataset = open(PathToFile,'r').readlines()
        temp1 = lista[iterration]
        temp2 = lista[iterration+1]
        dataset = dataset[temp1:temp2]
    except:
        break
    
    #lines = dataset.split("\n")
    iterration+=1
    lines = dataset
    


    for line in lines:
        if len(line) > 1:
            
            sample,aax,aay,aaz,xx,yy,zz = line.split(',')
            t.append(float(sample))
            ax.append(float(aax)-0.1044676)
            ay.append(float(aay)+0.0477295)
            az.append(float(aaz)-0.9561013)

            x.append(float(xx)+4.5992367)
            y.append(float(yy)+43.36626)
            z.append(float(zz)-1.5074805)



    window_length = 128;
    window = np.hamming(window_length);
    signal = [ax,ay,az,x,y,z]
    fs = 200
    for i in signal:
        #window = np.kaiser(window_length,5);
        overlap = math.floor(window_length*0.5-1);
        fft_length = window_length*2;
        stft_frequency, stft_time, signal_stft = sp.stft(i,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
        signal_stft = signal_stft[0:window_length-1,:];
        stft_frequency = stft_frequency[0:window_length-1];
        signal_stft_abs = abs(signal_stft);


        plt.figure();
        plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest');
        plt.ylabel('Frequency (Hz)');
        plt.xlabel('Time (s)');

        plt.show()

