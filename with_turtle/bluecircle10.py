import turtle
turtle.bgcolor('black')
turtle.speed(.1)
turtle.pensize(0.1)
turtle.pencolor('blue')

def drawcircle(radius):
    for i in range(20):
        if radius%2==0:
            turtle.pencolor('green')
        else:
            turtle.pencolor('blue')
        turtle.circle(radius)
        radius=radius-7
def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

drawdesign()
turtle.done()