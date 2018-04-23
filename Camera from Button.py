from picamera import PiCamera
from time import sleep
from gpiozero import Button
from gpiozero import LED

led = LED(20)
camera = PiCamera()
button = Button(18)

camera.start_preview(alpha=200)

for i in range(5):
    button.wait_for_press()
    sleep(1)
    
    camera.capture("/home/pi/button{0}.jpg".format(i))
    

camera.stop_preview()
