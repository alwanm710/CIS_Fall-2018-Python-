def getInteger(message,low,high):
    validInput = False
    while not(validInput):
        integerCandidate= input(message +" between "+str(low)+ " and "+ str(high)+ "\n")
        try:
            intReturn = int(integerCandidate)
            if (intReturn >= low and intReturn <= high):
                return intReturn
        except:
            validInput =False

#main
temp = getInteger("Enter temperature in farenheight",0,212)
print("You entered a temperature of",temp)


#Personal Note:
#ch06(1), Slide 26
