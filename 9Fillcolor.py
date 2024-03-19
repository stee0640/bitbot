import turtle
colors = ["red", "yellow", "green", "blue", "purple"]

def cirkel(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

for i in reversed(range(10)):
    cirkel((i+1)*10, colors[i % len(colors)])

turtle.exitonclick()

