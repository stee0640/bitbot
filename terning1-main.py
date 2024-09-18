from microbit import *
import random

def terning_slag():
    terning = random.randint(1,6)
    display.show(terning)
        
while True:
    if button_a.was_pressed() or button_b.was_pressed():
        terning_slag()
    
