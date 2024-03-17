import turtle

def firkant(skridt):
    for i in range(4):
        turtle.forward(skridt)
        turtle.right(90)

def blomst():
    for i in range(10):
        firkant(100)
        turtle.right(36)

blomst()
turtle.exitonclick()
