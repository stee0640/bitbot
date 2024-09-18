from microbit import *
import neopixel
import random
import music

def stop_left():
    pin16.write_digital(0)
    pin8.write_digital(0)

def stop_right():
    pin14.write_digital(0)
    pin12.write_digital(0)

def drive_left(dir):
    pin16.write_digital(1-dir)
    pin8.write_digital(dir)

def drive_right(dir):
    pin14.write_digital(1-dir)
    pin12.write_digital(dir)
    
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (0,255,255)
magenta = (255,0,255)
yellow = (255,255,0)
colors = [red, green, blue, cyan, magenta, yellow]

np = neopixel.NeoPixel(pin13, 12)

display.show(Image.HAPPY)
sleep(2000)
pin0.write_digital(0)
music.play(music.PYTHON, wait=False)    
display.clear()
drive_left(0)
counter = 0
for counter2 in range(800):
    if counter == 25:
        display.show(Image.HEART)
    elif counter == 50:
        display.clear()
        counter = 0
    if counter2 == 400:
        stop_left()
        drive_right(0)
    pixel = random.randint(0,11)
    np[pixel] = random.choice(colors)
    np.show()
    sleep(20)
    counter += 1
stop_right()
pin0.write_digital(0)
np.clear()
display.scroll("FARVEL")
display.show(Image.SKULL)
music.play(music.FUNERAL)
music.stop()
pin0.write_digital(0)
while True:
    pass
