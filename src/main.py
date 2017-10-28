#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep



# r = [255, 0, 0]
# g = [0,255,0]
# w = [255, 255, 255]

def get_names():
    names = [
        "lO_sprite_stage1.png",
        "lO_sprite_stage2.png",
        "lO_sprite_stage3.png",
        "lO_sprite_stage4.png",
        "lO_sprite_stage5.png",
        "lO_sprite_stage6.png",
        "lO_sprite_stage7.png",
        "lO_sprite_stage8.png",
        "lO_sprite_stage9.png",
    ]
    return names
    
if __name__ == "__main__":
    sense = SenseHat()
    sense.set_rotation(180)
    list_name = get_names()
    while True:
        for x in list_name:
            sleep(0.7) # Time in seconds.
            print('"{}"'.format(x))
            sense.load_image('"{}"'.format(x))




