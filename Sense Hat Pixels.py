from sense_hat import SenseHat
from time import sleep
from random import random

    
sense = SenseHat()

sense.clear()

Yellow = (255,255,0)

#sense.show_message("Picademy", text_colour=Yellow, back_colour=Blue)

j=0
k=0



while k<8:
    while j<8: 
        sense.set_pixel(j,k,Yellow)
        sleep(.05)
        j = j+1
    k = k+1
    j = 0

r = (255, 0, 0)
dr = (240, 0, 0)
w = (255, 255, 255)
g = (0,255,0)
pi= [
    w, g, g, w, w, g, g, w,
    w, w, g, g, g, g, w, w,
    w, r, r, r, r, r, r, w,
    w, r, r, r, r, r, r, w,
    w, r, r, r, r, r, r, w,
    w, w, r, r, r, r, w, w,
    w, w, r, r, r, r, w, w,
    w, w, w, r, r, w, w, w,
    ]

sense.set_pixels(pi)

