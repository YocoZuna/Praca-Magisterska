import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.impute import SimpleImputer
import os 
from scipy.fft import rfft, rfftfreq
#importing data set
#dataset = open("test.csv",'r').read()
first_sample = 1280
lista = [ ]
listsize = 0
try:
    dataset = open("ReadImu.csv",'r').readlines()
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
i = 0
while i <= lenth:
    try:
        dataset = open("ReadImu.csv",'r').readlines()[lista[i]:lista[i+1]]
    except:
        break
    
    #lines = dataset.split("\n")
    i+=1
    lines = dataset
    
    t = []
    ax=[]
    ay = []
    az = []
    x = []
    y = []
    z = []


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
       

    xyfft = rfft(x)
    xxfft = rfftfreq(128, 1/200)

    #lt.figure()
    #plt.plot(t, x)
    plt.figure()
    plt.plot(xxfft, np.abs(xyfft))
    plt.ylim(0,30)

plt.show()
 