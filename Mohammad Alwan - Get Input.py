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
number = getInteger("Enter number of times to loop",1,10)
print(number)


#Personal Note:
#ch06(1), Slide 26
