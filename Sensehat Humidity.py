from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    '''humidity = sense.get_humidity()
    print(humidity)

    if humidity > 34:
        w=(255,255,0)
    else:
        w=(0,0,255)
'''
    r = (255, 0, 0)
    dr = (240, 0, 0)
    w = (255,0,0)
    g = (0,255,0)
    
    pi= [
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    w, w, w, w, w, w, w, r,
    ]

    x=0
    while x<8:
        test=pi[(0,x)]
        x=x+1

    sense.set_pixels(pi)

    sleep(0.5)
