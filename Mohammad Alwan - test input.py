##integer1 = int(input("enter an integer \n"))
##
##
###Personal Note:
###ch06(1), Slide 24

def isInteger(integerCandidate):
    try:
        intReturn = int(integerCandidate)
        return True
    except:
        return False  

validInput = False
while not(validInput):
    integer1 = input("enter an integer \n")
    if isInteger(integer1):
        integer1 = int(integer1)
        print("Is an integer")
        validInput = True #(Or "break")
    else:
        print ("Not an integer - Try again")
print("That's all folks")



#Personal Note:
#ch06(1), Slide 25
