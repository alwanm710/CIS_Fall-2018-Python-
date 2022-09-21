#Mohammad Alwan, Program Ex.8-2 (Lottery)

from random import *

Amount_Of_Number = 7
LotteryNumber = Amount_Of_Number + 1
myArray = [0] * LotteryNumber

for index in range(1,LotteryNumber):
    randomNumber = randint(1, 9)
    while randomNumber in myArray:
        randomNumber = randint(1, 9)
    myArray[index] = randomNumber
print(myArray)

