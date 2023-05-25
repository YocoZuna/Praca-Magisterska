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
first_sample = 1280
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
    ay = []
    az = []
    gx = []
    gy = []
    gz = []




    for line in lines:
        if len(line) > 1:
            line = line[2:-4]
            sample,aax,aay,aaz,xx,yy,zz = line.split(';')
            t.append(float(sample))
            ax.append(float(aax)-0.1044676)
            ay.append(float(aay)+0.0477295)
            az.append(float(aaz)-0.9561013)

            gx.append(float(xx)+4.5992367)
            gy.append(float(yy)+43.36626)
            gz.append(float(zz)-1.5074805)


            



            """FFT"""
            
       
    axyfft = rfft(gx)
    axfft = rfftfreq(len(gx), 1/500)

    ayyfft = rfft(gy)
    ayfft = rfftfreq(len(gy), 1/500)

    azyfft = rfft(gz)
    azfft = rfftfreq(len(gz), 1/500)
   
    """    fft = [ax,ay,az] 


    axyfft = rfft(fft[0])
    axfft = rfftfreq(len(fft[0]), 1/200)

    ayyfft = rfft(fft[1])
    ayfft = rfftfreq(len(fft[1]), 1/200)

    azyfft = rfft(fft[2])
    azfft = rfftfreq(len(fft[2]), 1/200)
    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    plt.title("Acc")
    plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
    plt.savefig(f"Smietnik\\Acc_FFT{count}.png")
    plt.figure(1).clear()
    count = count+1"""

    print(f" Time_Start {t[0]}\n Time_End {t[-1]}\n")
    plt.figure(1)
    #plt.figure(figsize=(150,75)) ### Re-size (2,2) means 200x200 pixels .. Also wie have to sue plt.axis('off') to turn of the axis lines
    #plt.axis('off')
    plt.title("Acc")
    #plt.plot(axfft, np.abs(axyfft))
    plt.plot(ayfft, np.abs(ayyfft))
    #plt.plot(azfft, np.abs(azyfft))
    plt.legend(['Ax','Ay','Az'])
 
    #plt.savefig("Dupal.png")
    """SDFT"""

    window_length = 256;
    window = np.hamming(window_length);
    signal = gy
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);


    plt.figure(2);
    plt.title('Gy')
    figure_STFT_Gy = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_green);
    fig2 = plt.figure(2);
    fig2.canvas.draw()
    data2 = np.frombuffer(fig2.canvas.tostring_rgb(), dtype=np.uint8)
    data2 = data2.reshape(fig2.canvas.get_width_height()[::-1] + (3,))
    data2 = data2[58:428,80:577,:]

    signal = gz
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);

    plt.figure(3);
    plt.title('Gz')
    figure_STFT_Gz = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_blue);
    fig3 = plt.figure(3);
    fig3.canvas.draw()
    data3 = np.frombuffer(fig3.canvas.tostring_rgb(), dtype=np.uint8)
    data3 = data3.reshape(fig3.canvas.get_width_height()[::-1] + (3,))
    data3 = data3[58:428,80:577,:]

    im = plt.figure(3)
        
    signal = gx
    fs = 500


    #window = np.kaiser(window_length,5);
    overlap = math.floor(window_length-1);
    fft_length = window_length*2;
    stft_frequency, stft_time, signal_stft = sp.stft(signal,fs=fs,window=window,nperseg=window_length,noverlap=overlap,nfft=fft_length,return_onesided=False);
    signal_stft = signal_stft[0:window_length-1,:];
    stft_frequency = stft_frequency[0:window_length-1];
    signal_stft_abs = abs(signal_stft);

    plt.figure(4);
    plt.title('Gx')
    figure_STFT_Gx = plt.pcolormesh(stft_time, stft_frequency, signal_stft_abs, shading='nearest', cmap = my_cmap_red);
    fig4 = plt.figure(4);
    fig4.canvas.draw()
    data4 = np.frombuffer(fig4.canvas.tostring_rgb(), dtype=np.uint8)
    data4 = data4.reshape(fig4.canvas.get_width_height()[::-1] + (3,))
    data4 = data4[58:428,80:577,:]


    datargb = data2 + data3 + data4
    im = Image.fromarray(datargb)
    im.show()

    plt.ylabel('Frequency (Hz)');
    plt.xlabel('Time (s)');
    plt.show()
    plt.figure(1).clear()
    plt.figure(2).clear()
    plt.figure(3).clear()
    plt.figure(4).clear()
