from microbit import *
import neopixel
import random

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (0,255,255)
magenta = (255,0,255)
yellow = (255,255,0)
colors = [red, green, blue, cyan, magenta, yellow]

np = neopixel.NeoPixel(pin13, 12)

while True:
    pixel = random.randint(0,11)
    np[pixel] = random.choice(colors)
    np.show()
    sleep(20)