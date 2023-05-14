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
PathToFile = "ReadImu.csv"

try:
    dataset = open(PathToFile,'r').readlines()
    listsize = len(dataset)
    print(listsize)
except:
    print("Could not open CSV file\n")
    
temp = 0

for i in dataset:
    if i == '\n':
        dataset.remove('\n') 


for i in range(0,(int(listsize/128))):
    
    lista.append(temp)
    temp = temp +128



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





        axyfft = rfft(x)
        axfft = rfftfreq(len(x), 1/500)

        ayyfft = rfft(y)
        ayfft = rfftfreq(len(y), 1/500)

        azyfft = rfft(az)
        azfft = rfftfreq(len(z), 1/500)




        plt.figure(1)
        plt.title("Acc")
        plt.plot(axfft, np.abs(axyfft))
        plt.plot(ayfft, np.abs(ayyfft))
        plt.plot(azfft, np.abs(azyfft))
        plt.legend(['Ax','Ay','Az'])
  


    #plt.figure(1).clear()

    plt.show()   


 