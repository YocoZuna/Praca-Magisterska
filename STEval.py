import serial 
import time

class ST_EVal:
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
        """
        self.stEVAL_CMD

        description: dictionary with commands in byte format which have to be send to control the motor
        """
        self.stEVAL_CMD = {
            "START" : bytearray(b')\x00\x00\xe0\x19\x00'),
            
            "STOP" : bytearray(b')\x00\x00\xe0\x21\x00'),
            "FAULTACK" : bytearray(b')\x00\x00\xe0\x39\x00'),
            
            "PING" : bytearray(b'\x06\x00\x00`'),
            "BEACON" : bytearray(b'\x05\xc3\x00`'),

            "READ_REGISTER" : bytearray(b'\x49\x00\x00\x70\x11\x00'),
            "READ_ALL_REGISTERS" : bytearray(b'\xc9\x04\x00\xe0\x11\x00\x19\x00Y\x00Y\x1b\x99\x00\xd9\x00\x19\x01\x91\t\x91\x02\xd1\x02Q\t\x91\x01\xd1\x01\x91\x14Q\x14\x91\x00\xd1\x00\x11\t\xd1\x08\xd1\x05\x91\x05\xd1\x07\x11\x08Q\x03\x91\x03\x91\x04Q\x04\x11\x19\xd1\x18\x91\x0bQ\x0b\xd1\x0b\x11\x0cQ\x0c\x91\x0cI\x00\x89\x00\xc9\x00')
                                                                        
        }


        self.STEval  = serial.Serial(port=self.portCOM,baudrate=self.baudrate)

    def STEval_Init(self):
        """
        STEval_Init()
        return: NONE
        param: None
        description: Initlialize motor according to STM Motor SDK 6.1 ASEP protocol
        """

        self.STEval.write(self.stEVAL_CMD["PING"])
        time.sleep(1/10)
        self.STEval.write(self.stEVAL_CMD["BEACON"])
        time.sleep(1/10)
        self.STEval.write(self.stEVAL_CMD["PING"])
        time.sleep(1/10)
        self.STEval.write(self.stEVAL_CMD["FAULTACK"])
        time.sleep(1/10)

    def STEval_Motor_Start(self):
        """
        STEval_Start()
        return: NONE
        param: None
        description: starts the motor
        """

        self.STEval.write(self.stEVAL_CMD["START"])
        time.sleep(1/10)

    def STEval_Motor_Stop(self):
        """
        STEval_Stop()
        return: NONE
        param: None
        description: stops the motor
        """
        self.STEval.write(self.stEVAL_CMD["STOP"])
        time.sleep(1/10)

    def STEval_DeInit(self):
        """
        STEval_DeInit()
        return: NONE
        param: None
        description: deinitialize STMEval controler and close portCOM
        """
        self.STEval.close()


    def STEval_ChangeSpeed(self,speed):
        """
        STEval_ChangeSpeed(param)
        return: NONE
        param: Value in rpm 
        description : Changes the speed of motor controled by STMEval board with Motor SDK 6.1 firmware
        """
        self.header = b'\xc9\x00\x00\xc0\x08\x00\xa9\x01\x06\x00'
        
        self.tail = b'\x00\x00\x00\x00'
        self.lower = (speed&0xFF00)>>8
        self.higher = (speed&0xFF)
        self.temp = bytearray()
        self.temp.append(self.higher)
        self.temp.append(self.lower)
        self.STEval.write(self.header+self.temp+self.tail)
        time.sleep(1/10)

    def ST_Eval_ReadRegister(self,register):
        

   
   
        self.STEval.write(self.stEVAL_CMD["READ_ALL_REGISTERS"])
        self.buffor = self.STEval.read(80)
        print(self.buffor)


