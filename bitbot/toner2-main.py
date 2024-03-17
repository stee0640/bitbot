from microbit import *
import music

toner = [ "C", "E", "G", "E" ]

# C4 = Tone "C", Register "4"
for register in ["3", "4", "5", "6", "7", "8"]:
    for tone in toner:
        tone_register = tone + register 
        music.play(tone_register)
