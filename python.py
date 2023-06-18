
import threading
var = 1 
while(1):
    
    print(var)
    def CheckIfVarChanged(param):
        check = param
        check  = input()    
        return check

    ryn  =threading.Thread(target=CheckIfVarChanged(var),daemon=True )
    var = ryn



