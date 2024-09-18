from microbit import *
import random

def terning_slag():
    terning = random.randint(1,6)
    display.show(terning)
    
def animation(antal):
    for i in range(antal):
        terning_slag()
        sleep(100)
        
while True:
    if button_a.was_pressed() or button_b.was_pressed():
        animation(10)
        terning_slag()
    
