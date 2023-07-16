import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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

try:
    dataset = open(PathToFile,'r').readlines()
    listsize = len(dataset)

except:
    print("Could not open CSV file\n")


t_temp = []
ax_temp=[]
max_temp = []
ay_temp = []
az_temp = []
x_temp = []
y_temp = []
z_temp = []
pa_RGB = []
pb_RGB =[]
pc_RGB = []

for line in dataset:
        if len(line) > 1:
            line = line[3:len(line)-3]
            
            sample,aax,aay,aaz,xx,yy,zz,phasea,phaseb,phasec = line.split(',')
            t_temp.append(float(sample))
            ax_temp.append(float(aax)-0.1044676)
            ay_temp.append(float(aay)+0.0477295)
            az_temp.append(float(aaz)-0.9561013)

            x_temp.append(float(xx)+4.5992367)
            y_temp.append(float(yy)+43.36626)
            z_temp.append(float(zz)-1.5074805)
            
            pa_RGB.append(float(phasea))
            pb_RGB.append(float(phaseb))
            pc_RGB.append(float(phasec))

minima = np.min(pa_RGB)
pa_RGB = [x - minima for x in pa_RGB]
maxima = np.max(pa_RGB)
pa_RGB = [x * (255/maxima) for x in pa_RGB]

minima = np.min(pb_RGB)
pb_RGB = [x - minima for x in pb_RGB]
maxima = np.max(pb_RGB)
pb_RGB = [x * (255/maxima) for x in pb_RGB]

minima = np.min(pc_RGB)
pc_RGB = [x - minima for x in pc_RGB]
maxima = np.max(pc_RGB)
pc_RGB = [x * (255/maxima) for x in pc_RGB]

for i in range(0,len(pa_RGB)):
    pa_RGB[i] = int(np.round(pa_RGB[i]))
    pb_RGB[i] = int(np.round(pb_RGB[i]))
    pc_RGB[i] = int(np.round(pc_RGB[i]))

# dataset = open(PathToFile,'r').readlines()
# phasea,phaseb,phasec = line.split(',')


temp = 0
for i in range(0,(int(listsize/256))):
    
    lista.append(temp)
    temp = temp +256

lenth = len(lista)
iterration= 0
add_zeros_pa = 0
add_zeros_pb = 1
add_zeros_pc = 1
while iterration <= lenth:
    try:
        dataset = open(PathToFile,'r').readlines()
        temp1 = lista[iterration]
        temp2 = lista[iterration+1]
        dataset = dataset[temp1:temp2]
        pa_temp = pa_RGB[temp1:temp2]
        pb_temp = pb_RGB[temp1:temp2]
        pc_temp = pc_RGB[temp1:temp2]
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

    for i in range(0, len(pa_RGB)):
        pa_temp.insert(add_zeros_pa+1, 0)
        pa_temp.insert(add_zeros_pa+2, 0)
        add_zeros_pa = add_zeros_pa + 3

    for i in range(0, len(pb_RGB)):
        pb_temp.insert(add_zeros_pb-1, 0)
        pb_temp.insert(add_zeros_pb+1, 0)
        add_zeros_pb = add_zeros_pb + 3

    for i in range(0, len(pc_RGB)):
        pc_temp.insert(add_zeros_pc-1, 0)
        pc_temp.insert(add_zeros_pc-1, 0)
        add_zeros_pc = add_zeros_pc + 3
    
    pa_temp = np.asarray(pa_temp)
    pa_temp = pa_temp.astype(np.uint8)
    np.resize(pa_temp, (16,16,3))

    pb_temp = np.asarray(pb_temp)
    pb_temp = pb_temp.astype(np.uint8)
    np.resize(pb_temp, (16,16,3))

    pc_temp = np.asarray(pc_temp)
    pc_temp = pc_temp.astype(np.uint8)
    np.resize(pc_temp, (16,16,3))

    print(f" Time_Start {t[0]}\n Time_End {t[-1]}\n") 
 
    imr = Image.fromarray(pa_temp)
    img = Image.fromarray(pb_temp)
    imb = Image.fromarray(pc_temp)

    imr.show()
    img.show()
    imb.show()

    plt.figure(1)
    plt.plot(t, pa,'r')

    #plt.plot(t,y,'b')
    #plt.plot(t,z,'g')
    plt.show()
    
    #plt.ylim(-17,17)
        
    #os.remove("C:\\Users\\dawid\\Desktop\\Python\\test.csv")
    
    # Creating vectors X and Y where Y is predicted value X input values  