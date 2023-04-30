import turtle
t1=turtle.Turtle()
turtle.bgcolor('lightgreen')
t1.speed(1)
t1.pensize(3)
t1.color('red')
r=50
for i in range(3):
    t1.begin_fill
    t1.circle(r)
    r+=25
    t1.end_fill()
turtle.done()