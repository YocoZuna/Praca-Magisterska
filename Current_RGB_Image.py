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
            





        # For Sine Function
        """    axis[0, 0].plot(t, ax)
            
            plt.ylim(-1,1)
            axis[0, 0].set_title("Ax")
            #plt.savefig('my_plot.png')
            axis[1, 0].plot(t, ay)
            plt.ylim(-1,1)
            axis[1, 0].set_title("Ay")
            #plt.savefig('my_plot.png')
            axis[2, 0].plot(t, az)
            plt.ylim(-1,1)
            axis[2, 0].set_title("Az")
            #plt.savefig('my_plot.png')
            # For Cosine Function
            axis[0, 1].plot(t,x)
            plt.ylim(-1,1)
            axis[0, 1].set_title("Gx")
            #plt.savefig('my_plot.png')
            axis[1, 1].plot(t, y)
            plt.ylim(-1,1)
            axis[1, 1].set_title("Gy")
            #plt.savefig('my_plot.png')
            axis[2, 1].plot(t, z)
            plt.ylim(-1,1)
            axis[2, 1].set_title("Gz")
            #plt.savefig('my_plot.png')
            plt.ylim(-1,1)
        """

    plt.figure(1)
    plt.plot(t, pa,'r')

    #plt.plot(t,y,'b')
    #plt.plot(t,z,'g')
    plt.show()


    
    #plt.ylim(-17,17)
        
    #os.remove("C:\\Users\\dawid\\Desktop\\Python\\test.csv")
    
    # Creating vectors X and Y where Y is predicted value X input values  