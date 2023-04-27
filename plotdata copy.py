import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.impute import SimpleImputer
#importing data set
#dataset = open("test.csv",'r').read()
lista = [0,128,256,384,512,640,768,896]
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

    # Initialise the subplot function using number of rows and columns


    for line in lines:
        if len(line) > 1:
            
            sample,aax,aay,aaz,xx,yy,zz = line.split(',')
            t.append(float(sample))
            ax.append(float(aax)+0.4)
            ay.append(float(aay)+0.5)
            az.append(float(aaz)-0.4)
            x.append(float(xx))
            y.append(float(yy)+43)
            z.append(float(zz))






    # For Sine Function
   
    plt.figure(i)
    plt.title("Accelelometr")
    plt.plot(t, ax)
    plt.plot(t, ay)
    plt.plot(t, az)
    plt.legend()
    plt.savefig(f"ACC\\{i}.png")

    plt.figure(i+1)
    plt.title("Gyroscope")
    plt.plot(t, x)
    plt.plot(t, y)
    plt.plot(t, z)
    plt.legend()
    plt.savefig(f"Gyro\\{i}.png")
    plt.figure(i).clear()
    plt.figure(i+1).clear()
    #plt.savefig('my_plot.png')
 



# Creating vectors X and Y where Y is predicted value X input values  