import explorerhat
from time import sleep
from random import random

def forward (channel, event):
    explorerhat.light.blue.on()
    explorerhat.motor.one.forward(100)
    sleep(5)
    explorerhat.light.blue.off()
    explorerhat.motor.one.stop()

def backward (channel, event):
    explorerhat.light.red.on()
    explorerhat.motor.one.backward(100)
    sleep(5)
    explorerhat.light.red.off()
    explorerhat.motor.one.stop()

def random(channel, event):
    explorerhat.light.green.on()
    explorerhat.motor.one.backward(randint(20,100))
    sleep(randint(1,6))
    explorerhat.light.green.off()
    explorerhat.motor.one.stop()

explorerhat.touch.one.pressed(forward)
explorerhat.touch.three.pressed(backward)
explorerhat.touch.four.pressed(random)

'''
explorerhat.light.off()

explorerhat.light.green.on()
explorerhat.motor.one.forward(100)
sleep(5)
explorerhat.light.green.off()
explorerhat.motor.one.stop()

explorerhat.light.red.on()
explorerhat.motor.one.backward(100)
sleep(5)
explorerhat.light.red.off()
explorerhat.motor.one.stop()

'''
