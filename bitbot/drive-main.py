from microbit import *

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

while True:
    for i in range(2):
        drive_left(i)
        drive_right(i)
        sleep(3000)
        stop_left()
        stop_right()
        sleep(3000)
    

