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
age = getInteger("Enter your age",0,120)
if age > 50:
    print("Older than dirt")
else:
    print("Nice and young")


#Personal Note:
#ch06(1), Slide 26
