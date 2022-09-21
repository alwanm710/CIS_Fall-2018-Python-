from turtle import *
def bobSimpleCircle(t): #how I first did my turtle circle functions/module
    for i in range(360):     #circle has 360 so rotate one degree at a time 
        t.forward(1)	           #move forward 1 each time rotate
        t.right(1)      

bob=Turtle()  #Object oriented programming that we will do at end of class
bob.shape('turtle')
bob.pendown()
bob.color('green')
bobSimpleCircle(bob)
#but Python has function already

bob.penup()
bob.forward(50)
bob.color("blue")
bob.pendown()
bob.circle(60)


#Personal Note:
#ch06(1), Slide 17
