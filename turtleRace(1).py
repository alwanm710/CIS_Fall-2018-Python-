from random import randint
from turtle import *  # input all public methods,etc from turtle class
myWindow = Screen()     # don't have to use class name "turtle." in front of function calls 
ts = getscreen()      # that is to left no turtle.Screen() or bob=turtle.Turtle() below
finish = ts.window_width()

bob = Turtle()
bob.color("blue")
bob.shape("turtle")
bob.penup()
bob.setpos((-finish/2)+10,50)
bob.pendown()
bob.speed(1)

roger = Turtle()
roger.color("red")
roger.shape("turtle")
roger.penup()
roger.setpos((-finish/2)+10,-50)
roger.pendown()
roger.speed(1)

bobXCor = 0
rogXCor = 0
finish = finish - 35
winner = False
while not(winner):
    bMove = randint(1,10)
    bobXCor = bobXCor + bMove
    bob.forward(bMove)
    rMove = randint(1,10)
    rogXCor = rogXCor + rMove
    roger.forward(rMove)
    if bobXCor > finish and rogXCor > finish:
        print ("a Tie")
        winner = True
    elif bobXCor > finish:
        print ("bob wins")
        winner = True
    elif rogXCor > finish:
        print ("roger wins")
        winner = True

    

