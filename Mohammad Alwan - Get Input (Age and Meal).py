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
            
def getFloat(message,low,high):
    validInput = False
    while not(validInput):
        floatCandidate= input(message +" between "+str(low)+ " and "+ str(high)+ "\n")
        try:
            floatReturn = float(floatCandidate)
            if (floatReturn >= low and floatReturn <= high):
                return floatReturn
        except:
            validInput =False

#main
#main
age = getInteger("Enter your age",0,120)
if age > 50:
    print("Older than dirt")
else:
    print("Nice and young")

price = getFloat("Enter price of meal",1.00,200.00)
if price <= 10.00:
    print("Nice price")
else:
    print("Too much money - going to McDonald's")


#Personal Note:
#ch06(1), Slide 26

