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
PathToFile = "Data_test_1024_samples.txt"

cm = Colormap()
my_cmap_red = cm.cmap_bicolor('black', 'red')
my_cmap_green = cm.cmap_bicolor('black', 'green')
my_cmap_blue = cm.cmap_bicolor('black', 'blue')

try:
    dataset = open(PathToFile,'r').readlines()
    listsize = len(dataset)

except:
    print("Could not open CSV file\n")

example =[]

for i in range(0,(int(listsize))):
    
    lista.append(temp)
    temp = temp +1

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

for line in dataset:
        if len(line) > 1:
            line = line[3:len(line)-3]
            
            sample,aax,aay,aaz,xx,yy,zz,phasea,phaseb,phasec = line.split(',')
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

minima = min(pa)
maxima = max(pa)
# dataset = open(PathToFile,'r').readlines()
# phasea,phaseb,phasec = line.split(',')

lista.clear()
t.clear()
ax.clear()
max.clear()
ay.clear()
az.clear()
x.clear()
y.clear()
z.clear()
pa.clear()
pb.clear()
pc.clear()

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
    max = []
    ay = []
    az = []
    x = []
    y = []
    z = []
    pa = []
    pb =[]
    pc = []

    for line in dataset:
        if len(line) > 1:
            line = line[3:len(line)-3]
            
            sample,aax,aay,aaz,xx,yy,zz,phasea,phaseb,phasec = line.split(',')
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
    
    print(f" Time_Start {t[0]}\n Time_End {t[-1]}\n") 

    plt.figure(1)
    plt.plot(t, pa,'r')

    #plt.plot(t,y,'b')
    #plt.plot(t,z,'g')
    plt.show()


    
    #plt.ylim(-17,17)
        
    #os.remove("C:\\Users\\dawid\\Desktop\\Python\\test.csv")
    
    # Creating vectors X and Y where Y is predicted value X input values  