from STEval import ST_EVal
from STMF411RE import ST_F411
import threading
import time
buffor = []
def run_Thread(function):
    x = threading.Thread(target=function)
    return x


MotorContoler = ST_EVal("COM6",115200)
SensorReader = ST_F411("COM3",115200)

MotorContoler.STEval_Init()
MotorContoler.STEval_ChangeSpeed(3000)

MotorContoler.STEval_Motor_Start()
MotorContoler.STEval_ChangeSpeed(7000)
time.sleep(7)

threadSensorReader = run_Thread(SensorReader.ST_F411_Read_IMU(filePath="ReadImu.csv",buffor=buffor))






