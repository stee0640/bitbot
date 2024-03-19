import turtle
import random
colors = ["red", "green", "blue", "violet", "cyan", "magenta", "yellow", "pink"]
turtle.shape("turtle")
turtle.pensize(5)

def turn_and_move(length, angle, far_from_home):
    turtle.pencolor(random.choice(colors))
    if turtle.distance(0,0) >= far_from_home:
        turtle.setheading(turtle.towards(0,0))
    else:
        turtle.right(random.randint(0,1) * 2* angle - angle)
    turtle.forward(length)

while True:
    turn_and_move(length=10, angle=30, far_from_home=300)