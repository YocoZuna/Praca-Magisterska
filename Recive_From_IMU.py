from STMF411RE import ST_F411
buffor = []
SensorReader = ST_F411("COM3",921600,buffor=buffor)

while(1):
    SensorReader.ST_F411_Read_IMU(filePath="ReadImu.csv")