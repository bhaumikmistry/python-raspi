#!/usr/bin/python
from sense_hat import SenseHat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

from time import sleep
import pygame  # See http://www.pygame.org/docs
from pygame.locals import *

sense = SenseHat()
xbird = 3
ybrid = 3

# r = [255, 0, 0]
g = [0,255,0]
# w = [255, 255, 255]

def get_names():
    names = [
        "stage1.png",
        "stage2.png",
        "stage3.png",
        "stage4.png",
        "stage5.png",
        "stage6.png",
        "stage7.png",
        "stage8.png",
        "stage9.png",
    ]
    return names

def pushed_up(event):
    global ybrid
    if event.action != ACTION_RELEASED:
        print("up pressed ----->>")
        sense.set_pixel(xbird, ybrid, g)                      
        ybrid -= 1

def pushed_down(event):
    global ybrid
    if event.action != ACTION_RELEASED:
        print("up pressed ----->>")    
        sense.set_pixel(xbird, ybrid, g)                          
        ybrid += 1
        
def setBird(sense):
    sense.set_pixel(0, 0, red)

def check_bird():
    if ybrid > 7 && ybrid < 0:
        return False

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

def boom():
    sense.load_image("l0_boom1.png")
    sleep(0.3) # Time in seconds.
    sense.load_image("l0_boom2.png")
    sleep(0.3) # Time in seconds.
    sense.load_image("l0_boom3.png")
    sleep(0.3) # Time in seconds.
    sense.load_image("l0_boom4.png")
    sleep(0.3) # Time in seconds.
    sense.load_image("l0_boom5.png")
    sleep(0.3) # Time in seconds.
    sense.load_image("l0_boom6.png")
    sleep(0.3) # Time in seconds.
    

def main_unit():
    while True:
        list_name = get_names()
        for x in list_name:
            print('"{}"'.format(x))
        sense.clear()

        sense.load_image("stage1.png")
        sense.set_pixel(xbird, ybrid, g)     
        res = check_bird()
        if(!res):
            break
        sleep(0.7) # Time in seconds.
        sense.load_image("stage2.png")
        sense.set_pixel(xbird, ybrid, g)    
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage3.png")
        sense.set_pixel(xbird, ybrid, g)  
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage4.png")
        sense.set_pixel(xbird, ybrid, g)
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage5.png")
        sense.set_pixel(xbird, ybrid, g)
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage6.png")
        sense.set_pixel(xbird, ybrid, g)  
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage7.png")
        sense.set_pixel(xbird, ybrid, g) 
        if(!res):
            break

        sleep(0.7) # Time in seconds.
        sense.load_image("stage8.png")
        sense.set_pixel(xbird, ybrid, g)
        if(!res):
            break

        sleep(0.7) # Time in seconds.
    return True


if __name__ == "__main__":
    sense.set_rotation(180)
    while True:
        main_unit()
        boom()
        global ybrid = 3






