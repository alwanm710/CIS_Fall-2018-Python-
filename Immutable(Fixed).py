str = "Coffee"
strArray = [" "] * len(str)
for index in range(0,len(str)):
    strArray[index] = str[index]
    
strArray[0] = "T"
print(str, strArray)
