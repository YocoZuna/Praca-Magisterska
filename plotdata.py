import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.impute import SimpleImputer
#importing data set
#dataset = open("test.csv",'r').read()
lista = [0,128,256,384,512,640,768,896]

import os 
lenth = len(lista)
i = 0
while i <= lenth:
    try:
        dataset = open("test.csv",'r').readlines()[lista[i]:lista[i+1]]
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

    plt.figure()
    plt.plot(t, x,'r')
    plt.plot(t, y,'g')
    plt.plot(t, z)
 
    plt.ylim(-17,17)
    
#os.remove("C:\\Users\\dawid\\Desktop\\Python\\test.csv")
plt.show()
# Creating vectors X and Y where Y is predicted value X input values  