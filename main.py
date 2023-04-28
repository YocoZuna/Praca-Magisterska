from STEval import ST_EVal
from STMF411RE import ST_F411
import threading

MotorContoler = ST_EVal("COM6",115200)
SensorReader = ST_F411("COM3",115200)

MotorContoler.STEval_Init()





