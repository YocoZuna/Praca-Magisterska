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
PathToFile = "ReadImu.csv"
#PathToFile = "ReadImu.csv"
try:
    dataset = open(PathToFile,'r').readlines()
    listsize = len(dataset)
    print(listsize)
except:
    print("Could not open CSV file\n")
    
temp = 0
for i in range(0,(int(listsize/256))):
    
    lista.append(temp)
    temp = temp +256


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

    t_start = 0
    dt = 0.0025
    t_end=0.6400-dt;
    t=np.arange(start=t_start,stop=t_end-dt,step=dt)
    signal = gy
    signal_ft = np.fft.fft(signal);
    signal_ft_half_length = math.floor(len(signal_ft)/2);
    signal_ft = signal_ft/(signal_ft_half_length*2)*100;
    signal_ft = signal_ft[0:signal_ft_half_length-1];
    signal_ft_abs = abs(signal_ft);

    f=np.arange(0,signal_ft_half_length-1,1)*1/t_end;

    plt.figure();
    plt.step(f,signal_ft_abs, color = 'red');
    plt.xlabel('Frequency (Hz)');
    plt.ylabel('Power of signal component');
    plt.legend(['cosines of f=%g Hz sampled with dt=%g (s), tend=%g' % (1, dt, t_end)]);
    plt.show();