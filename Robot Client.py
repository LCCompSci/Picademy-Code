from gpiozero import DistanceSensor
from gpiozero import TrafficLights
from gpiozero import Button
from bluedot.btcomm import BluetoothClient
from time import sleep

forward = Button(20)

def print_bt_error():
    print ("Error - Check BT connection!")

def print_bt_error2():
    print ("Error 2- Check BT connection!")

def data_received(data):
    print (data)
    

c = BluetoothClient("baxbotserver", data_received)

#try:
#    c = BluetoothClient("baxbotserver", data_received)
#except:
#    print_bt_error()

    
while True:
    forward.wait_for_press()
    try:
        c.send("forward")
    except:
        print_bt_error2()

    forward.wait_for_stop()
    try:
        c.send("stop")
    except:
        print_bt_error2()
'''
# Create lights 
lights = TrafficLights(18, 15, 14)

# Start Listing to Distance Sensor
sensor = DistanceSensor(echo=12, trigger=11)

while True:
    distance = int(sensor.distance * 100)
    print('Distance: ',distance )


    if (distance < 20):
        lights.off()
        lights.red.on()
        
    elif (distance < 50):
        lights.off()
        lights.amber.on()
        
    else:
        lights.off()
        lights.green.on()

    sleep(.5)
   
'''



