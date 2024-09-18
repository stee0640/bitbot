from microbit import *
import random

def maybe_skull():
    if random.randrange(20) == 0:
        display.show(Image.SKULL)
        sleep(300)
        if button_a.is_pressed() or button_b.is_pressed():
            audio.play(Sound.GIGGLE)

while True:
    for i in Image.ALL_CLOCKS:
        display.show(i)
        sleep(50)
        if button_a.is_pressed() or button_b.is_pressed():
            audio.play(audio.SoundEffect())
        else:
            maybe_skull()
    
