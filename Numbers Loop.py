import sys
number = 6
while (number > 5):
    number = int(input(" Enter a number either > 5 or <= 5 to end the loop: ")) 
    if number <= 5:
            print ("you entered ", number, " which is <= 5, program ending")
    else:
            print("you entered", number)
print("That's all folks!")
