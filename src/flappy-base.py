#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep



# r = [255, 0, 0]
# g = [0,255,0]
# w = [255, 255, 255]

def get_names():
    names = [
        "/img/l0_sprite_stage1.png",
        "/img/l0_sprite_stage2.png",
        "/img/l0_sprite_stage3.png",
        "/img/l0_sprite_stage4.png",
        "/img/l0_sprite_stage5.png",
        "/img/l0_sprite_stage6.png",
        "/img/l0_sprite_stage7.png",
        "/img/l0_sprite_stage8.png",
        "/img/l0_sprite_stage9.png",
    ]
    return names


if __name__ == "__main__":
    sense = SenseHat()
    sense.set_rotation(180)
    list_name = get_names()
    while True:
        for x in list_name:
            sleep(0.7) # Time in seconds.
            print(x)
            sense.load_image(x)




