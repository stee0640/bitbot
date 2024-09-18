from microbit import *
import music

toner = [ "C", "E", "G", "E" ]

# C4:8 = Tone "C", Register "4", Slag "8"
for slag in ["0", "1", "2"]:
    for register in ["3", "4", "5", "6", "7", "8"]:
        for tone in toner:
            tone_register = tone + register 
            tone_register_slag = tone_register + ":" + slag
            music.play(tone_register_slag)
