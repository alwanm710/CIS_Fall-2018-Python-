#Get a test result
#In Python display and input together
validInput = False
while not(validInput):
    score = int(input("Enter the correct score: "))
    if score < 0 or score > 100: #alt not(score>=0 and score <=100)
        print("ERROR:  The score cannot be less than 0 ") 
        print("or greater than 100.")
    else:
        validInput = True #could have also put 'break' here to exit loop
#End While
