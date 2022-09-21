from turtle import Turtle
class MyTurtle(Turtle):   #Python subclass has superclass in ( ) no extends*
    def __init__(self, color, shape='turtle'):
        super(MyTurtle, self).__init__(shape=shape)
        self.color(color)

turtle1 = MyTurtle("blue")
turtle1.right(90)
turtle2 = MyTurtle("red")
turtle1.forward(100)
turtle2.forward(100)
