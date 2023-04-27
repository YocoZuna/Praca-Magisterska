import serial 
import time
from STEval import ST_EVal

sample = 0









stm32F411  = serial.Serial(port="COM3",baudrate=115200)
file = open("test.csv","a+")
print("Collecting data")
while(stm32F411.readable()):
    

    buffor=stm32F411.readline().decode('ascii')
    print(buffor)
    sample = sample+1
    file.write(f"{sample},{buffor}")

stm32F411.close()

##1843200