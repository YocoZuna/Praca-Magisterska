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
t = []
ax=[]
ay = []
az = []
x = []
y = []
z = []

lenth = len(lista)
i = 0
while i <= lenth:
    try:
        dataset = open(PathToFile,'r').readlines()[lista[i]:lista[i+1]]
    except:
        break
    
    #lines = dataset.split("\n")
    i+=1
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



    

    axyfft = rfft(ax)
    axfft = rfftfreq(len(ax), 1/200)

    ayyfft = rfft(ay)
    ayfft = rfftfreq(len(ay), 1/200)

    azyfft = rfft(az)
    azfft = rfftfreq(len(az), 1/200)




    plt.figure(1)
    plt.title("Acc")
    plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
    plt.show()


    plt.figure(1).clear()

       


 