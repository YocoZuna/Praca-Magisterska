import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.impute import SimpleImputer
#importing data set
#dataset = open("test.csv",'r').read()
lista = [ ]
listsize = 0
PathToFile = "ReadImu.csv"
buffor= [ ]
try:
    dataset = open(PathToFile,'r').readline()
    listsize = len(dataset)
    print(listsize)
except:
    print("Could not open CSV file\n")
    

buffor = dataset.split(',')

temp = 0






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
        datasett = buffor[temp1:temp2]
    except:
        pass
    
    #lines = dataset.split("\n")
    iterration+=1
    lines = datasett
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
            
            line = line[2:-4]
            sample,aax,aay,aaz,xx,yy,zz = line.split(';')
            t.append(float(sample))
            ax.append(float(aax)-0.1044676)
            ay.append(float(aay)+0.0477295)
            az.append(float(aaz)-0.9561013)

            x.append(float(xx)+4.5992367)
            y.append(float(yy)+43.36626)
            z.append(float(zz)-1.5074805)






    # For Sine Function
   
    plt.figure(1)
    plt.title("Acc")
    plt.plot(t, ax)
    plt.plot(t, ay)
    plt.plot(t, az)
    plt.legend(['Ax','Ay','Az'])
    plt.xlabel("Sample number")
    plt.ylabel("Readed value")
    plt.ylim(-5,5)
    #plt.savefig(f"Acc\\{i}.png")
    
    plt.figure(2)
    plt.title("Gyro")
    plt.plot(t, x)
    plt.plot(t, y)
    plt.plot(t, z)
    plt.legend(['Gx','Gy','Gz'])

    plt.xlabel("Sample number")
    plt.ylabel("Readed value")
    #plt.savefig(f"Gyro\\{i}.png")
    plt.show() 
    plt.figure(1).clear()
    plt.figure(2).clear()
    
    #plt.savefig('my_plot.png')
 



# Creating vectors X and Y where Y is predicted value X input values  