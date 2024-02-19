from microbit import *
import neopixel

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (0,255,255)
magenta = (255,0,255)
yellow = (255,255,0)
colors = [red, green, blue, cyan, magenta, yellow]

np = neopixel.NeoPixel(pin13, 12)

while True:
    for color in colors:
        for pixel in range(12):
            np[pixel] = color
            np.show()
            sleep(20)