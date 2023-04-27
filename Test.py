from STEval import ST_EVal
import time


xcx = ST_EVal("COM6",115200)

xcx.STEval_Init()
xcx.STEval_Motor_Start()

time.sleep(5)



xcx.STEval_ChangeSpeed(3000)
time.sleep(5)
xcx.STEval_ChangeSpeed(5000)
time.sleep(5)
xcx.STEval_ChangeSpeed(9600)
time.sleep(15)
xcx.STEval_ChangeSpeed(3000)
xcx.STEval_Motor_Stop()
xcx.STEval_DeInit()