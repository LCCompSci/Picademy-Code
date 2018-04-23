from sense_hat import SenseHat
from time import sleep

sense = SenseHat()



while True:
    data = sense.get_orientation()
    
    roll = data['roll']
    pitch = data['pitch']
    yaw = data['yaw']

    print ("The roll is", roll)
    print ("The pitch is", pitch)
    print ("The yaw is", yaw)
    print ("********************")
    sleep(2)


