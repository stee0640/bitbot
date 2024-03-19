import turtle

def x_kant(x):
    for i in range(x):
        turtle.forward(50)
        turtle.right(360/x)

x_kant(x=3)
x_kant(x=4)
x_kant(x=8)

turtle.exitonclick()