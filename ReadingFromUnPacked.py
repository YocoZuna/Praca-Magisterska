data = open("FTTYSD.txt","r")
ReadData = data.readline()
SplittedData = []

print(len(ReadData))
ReadData = ReadData[4:len(ReadData)-13]


SplittedData = ReadData.split('),')
for i in range(0,255):
    SplittedData[i] = SplittedData[1:len(SplittedData)]
print(ReadData)