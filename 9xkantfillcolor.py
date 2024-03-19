import turtle

def x_kant(x, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(x):
        turtle.forward(50)
        turtle.right(360/x)
    turtle.end_fill()

x_kant(x=8, color="blue")
x_kant(x=4, color="green")
x_kant(x=3, color="red")

turtle.exitonclick()