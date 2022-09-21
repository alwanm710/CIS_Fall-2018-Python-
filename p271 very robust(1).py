#Get a test result
#In Python display and input in one statement-should include range to users
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

validInput = False #guilty until proven innocent?
#Make sure it is not lower than 0. "#" instead of // Java as well as book pseudocode
while not(validInput):  
    score = input("Input score Enter a test score from 0 to 100:")
    if is_integer(score):
        score=int(score)
        if 0 <=  score <= 100: #deMorgan's theorem 
            validInput = True # valid input breaks out of loop 
    #not good    
    print("ERROR:  The score must be an integer and") #display --> print
    print("        cannot be less than 0 or greater than 100.")
#End While
