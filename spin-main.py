from microbit import *

def stop_right():
    pin14.write_digital(0)
    pin12.write_digital(0)

def drive_right():
    pin14.write_digital(1)
    pin12.write_digital(0)

drive_right()
sleep(3000)
stop_right()
    

