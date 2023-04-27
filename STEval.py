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


