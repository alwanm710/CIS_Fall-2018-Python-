from turtle import *
color('red', 'yellow')
begin_fill()
speed(10)
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


#Personal Note:
#ch06, slide 13
#Made it faster
#Added on line 4: "speed(10)"
