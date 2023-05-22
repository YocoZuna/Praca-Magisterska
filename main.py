from STEval import ST_EVal
from STMF411RE import ST_F411
import threading
import time
buffor = []




"""MotorContoler = ST_EVal("COM6",115200)


MotorContoler.STEval_Init()
MotorContoler.STEval_ChangeSpeed(2000)

MotorContoler.STEval_Motor_Start()
time.sleep(7)
MotorContoler.STEval_ChangeSpeed(6000)
time.sleep(1)
MotorContoler.ST_Eval_ReadRegister(2001)"""



SensorReader = ST_F411("COM3",921600,buffor)

SensorReader.ST_F411_Read_IMU(filePath="ReadImu.csv")



