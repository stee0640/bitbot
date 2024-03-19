import turtle
import random
stamps = []
turtle.penup()

def move_and_turn(length, angle, how_far):
    turtle.forward(length)
    if turtle.distance(0,0) >= how_far:
        turtle.setheading(turtle.towards(0,0))
    else:
        if  random.randint(0,1) == 0:
            turtle.right(angle)
        else:
            turtle.left(angle)

def stamp_and_record(snake_len):
    stamps.append(turtle.stamp())
    if len(stamps) >= snake_len:
        turtle.clearstamp(stamps.pop(0))

while True:
    move_and_turn(length=8, angle=30, how_far=300)
    stamp_and_record(snake_len=7)