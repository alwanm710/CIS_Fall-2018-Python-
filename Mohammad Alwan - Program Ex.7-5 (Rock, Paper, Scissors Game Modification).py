#Mohammad Alwan, Program Ex.7-5 (Rock, Paper, Scissors Modification)

from random import randint

def GetComputerPick():
    Number = randint(1,3)
    if Number == 1:
        return("rock")
    elif Number == 2:
        return("paper")
    else: #Know must be 3
        return("scissors")

def PlayGame(YourP, ComputerP):
    if YourP == ComputerP:
        return("It's a tie")
    elif YourP == "rock" and ComputerP == "paper":
        print("Paper covers rock so the computer wins")
    elif YourP == "rock" and ComputerP == "scissors":
        print("Rock crushes scissors so you win")
    elif YourP == "paper" and ComputerP == "rock":
        print("Paper covers rock so you win")
    elif YourP == "paper" and ComputerP == "scissors":
        print("Scissors cuts paper so the computer wins")
    elif YourP == "scissors" and ComputerP == "paper":
        print("Scissors cuts paper so you win")
    else: #YourP == "scissors" and ComputerP == "rock":
        print("Rock crushes scissors so the computer wins")



#Main
ComputerPick = GetComputerPick()
print("Lets Play!!")
YourPick = input("Rock, Paper, Scissors, Shoot!: ")

    #This while not loop will make sure the input is rock, paper, or scisser
while not(YourPick.lower() == "rock" or YourPick.lower() == "paper"or YourPick.lower() == "scissors"):
    print("Hey no cheating!!")
    YourPick = input("Please enter rock, paper, or scissors for your pick: ")

    #Displays the computers pick to player
print("The Computer picked",ComputerPick)

    #Displays the winner of the match
print("You picked",YourPick,"and the computer picked",ComputerPick)
WhoWon = PlayGame(YourPick, ComputerPick)
print(WhoWon)






