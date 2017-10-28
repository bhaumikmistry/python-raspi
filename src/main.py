#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep



# r = [255, 0, 0]
# g = [0,255,0]
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

if __name__ == "__main__":
    sense = SenseHat()
    sense.set_rotation(180)
    list_name = get_names()
    while True:
        for x in list_name:
            print('"{}"'.format(x))
        sense.clear()
        sense.load_image("stage1.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage2.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage3.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage4.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage5.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage6.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage7.png")
        sleep(0.7) # Time in seconds.
        sense.load_image("stage8.png")
        sleep(0.7) # Time in seconds.




