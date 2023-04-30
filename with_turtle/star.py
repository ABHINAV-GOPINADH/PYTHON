import turtle
turtle.bgcolor('blue')
turtle.speed(1)
turtle.pensize(3)
turtle.pencolor('red')
for j in range(2):
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.pendown()
    turtle.right(270)
turtle.done()