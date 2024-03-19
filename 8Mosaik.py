import turtle

def x_kant(x, size):
    for i in range(x):
        turtle.forward(size)
        turtle.right(360/x)


def mosaik():
    for i in range(10):
        x_kant(5, 50)
        x_kant(5, 100)
        turtle.right(36)

mosaik()
turtle.exitonclick()