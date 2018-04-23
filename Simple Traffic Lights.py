from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(14, 15, 18)

while True:
    lights.red.on()
    sleep(.5)
    lights.red.off()
    lights.amber.on()
    sleep(.5)
    lights.amber.off()
    lights.green.on()
    sleep(.5)
    lights.green.off()
