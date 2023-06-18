import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
from scipy import signal as sp 
import math
import os 
from scipy.fft import rfft, rfftfreq
import MovingAvrgFilter
from colormap import Colormap
from PIL import Image
MovingAvr = MovingAvrgFilter.Moving_Avgr_Filter()
count = 0
#importing data set
#dataset = open("test.csv",'r').read()
lista = [ ]
listsize = 0
temp = 0

cm = Colormap()
my_cmap_red = cm.cmap_bicolor('black', 'red')
my_cmap_green = cm.cmap_bicolor('black', 'green')
my_cmap_blue = cm.cmap_bicolor('black', 'blue')

PathToFile = "ReadImu.csv"
buffor= [ ]
try:
    dataset = open(PathToFile,'r').readline()
    listsize = len(dataset)
    

except:
    print("Could not open CSV file\n")


buffor = dataset.split(',')

for i in range(0,(int(listsize/256))):
    
    lista.append(temp)
    temp = temp +256


lenth = len(lista)
iterration= 0
while iterration <= lenth:
    try:
       
        temp1 = lista[iterration]
        temp2 = lista[iterration+1]
        datasett = buffor[temp1:temp2]
    except:
        break
    
    #lines = dataset.split("\n")
    iterration+=1
    lines = datasett
    
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


    for line in lines:
        if len(line) > 1:
            line = line[3:len(line)-3]
          
            sample,aax,aay,aaz,xx,yy,zz,phasea,phaseb,phasec = line.split(',')
            t.append(float(sample))
            ax.append(float(aax)-0.1044676)
            ay.append(float(aay)+0.0477295)
            az.append(float(aaz)-0.9561013)

            gx.append(float(xx)+4.5992367)
            gy.append(float(yy)+43.36626)
            gz.append(float(zz)-1.5074805)
            
            pa.append(float(phasea))
            pb.append(float(phaseb))
            pc.append(float(phasec))
            
       
    axyfft = rfft(gx)
    axfft = rfftfreq(len(gx), 1/500)

    ayyfft = rfft(gy)
    ayfft = rfftfreq(len(gy), 1/500)

    azyfft = rfft(gz)
    azfft = rfftfreq(len(gz), 1/500)
   

    print(f" Time_Start {t[0]}\n Time_End {t[-1]}\n")
    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    #plt.axis('off')
    plt.title("Acc")
    #plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    #plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
 

    plt.ylabel('Frequency (Hz)');
    plt.xlabel('Time (s)');
    plt.show()
    plt.figure(1).clear()
    plt.figure(2).clear()
    plt.figure(3).clear()
    plt.figure(4).clear()
