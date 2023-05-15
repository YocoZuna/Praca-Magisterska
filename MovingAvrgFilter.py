"""
Implementation of 4 point avr moving filter

"""

class Moving_Avgr_Filter:


    def __init__(self):
    

        self.moving_coeff = [
            0.0671380244098801,
            0.053625110441227655,
            -0.043207809012228045,
            0.03410057227903974,
            -0.02061381968084446,
            -0.001021497987272565,
            0.030930004500582645,
            -0.06676295206570804,
            0.10385538548795976,
            -0.13623714752218546,
            0.15836474672817386,
            0.8337540968056818,
            0.15836474672817386,
            -0.13623714752218546,
            0.10385538548795976,
            -0.06676295206570804,
            0.030930004500582645,
            -0.001021497987272565,
            -0.02061381968084446,
            0.03410057227903974,
            -0.043207809012228045,
            0.053625110441227655,
            0.0671380244098801


        ]
        """        for i in range(0,10):
                    self.moving_coeff.append(0.1)"""

        self.buff = []
        for y in range(0,len(self.moving_coeff)):
            self.buff.append(0.0) 
        self.buffIndex = 0
        self.out = 0

    def Filter_Fill(self,input):
        

        # Store latest sample in buffer
        self.buff[self.buffIndex] = input

        #Increment buffer index and wrap around if necessary

        self.buffIndex = self.buffIndex+1

        if self.buffIndex == len(self.moving_coeff):
            self.buffIndex = 0 
       
        self.out = 0

        self.sumIndex = self.buffIndex

        for n in range(0,len(self.moving_coeff)):

            if self.sumIndex > 0:
                self.sumIndex = self.sumIndex-1
            else:
                self.sumIndex = len(self.moving_coeff)-1

            self.temp1 = float(self.moving_coeff[n])
            self.temp2 = float(self.buff[self.sumIndex])

            self.out = self.out + self.temp1 * self.temp2
        return float(self.out)
