import serial 
import time




class ST_F411:
    """
    __init__(param1,param2)
    return: NONE
    param1: specify which portCOM open to communicate with STM32Eval
    param2: specify baudrate of communication 
    description: Initlialize motor according to STM Motor SDK 6.1 ASEP protocol
    """
    def __init__(self, portCOM, baudrate):
        self.portCOM = portCOM
        self.baudrate = baudrate
        self.sample = 0
        self.ST_F411  = serial.Serial(port=self.portCOM ,baudrate=self.baudrate)


    
    def ST_F411_Close_File(self,file):
        """
        ST_F411_Close_File(param1)
        return: NONE
        param1: file
        description: specify which file should be closed
        """
       
        self.temp = file.close()

    def ST_F411_Read_IMU(self,filePath,buffor):

        """
        ST_F411_Read_IMU(param1,param2)
        return: NONE
        param1: CSV file path in which data will be stored
        param2: buffor with data that arrived on portCom
        description: Read from portCOM and store the data in CSV file 
        """
        
        
        self.sample  =0
        self.buffor=self.ST_F411.write('s'.encode('ascii'))
        while(self.ST_F411.readable()):
            self.file = open(filePath,'a+')
            self.buffor=self.ST_F411.readline().decode('ascii')
            self.sample =  self.sample+1
            self.file.write(f"{self.buffor}")

    def ST_F411_DeInit(self):
        """
        STEval_DeInit()
        return: NONE
        param: None
        description: deinitialize ST_F411 controler and close portCOM
        """
        self.buffor=self.ST_F411.write('e'.encode('ascii'))
        self.ST_F411.close()

