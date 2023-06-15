xd = 0
bufforSize = 10280
sample = []
for i in range(0,int(bufforSize/40)):
   # print(xd)
    sample.append(xd)
    xd += 40
 

print(sample)
