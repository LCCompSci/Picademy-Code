from picamera import PiCamera

camera=PiCamera()
camera.image_effect = 'colorswap'
camera.start_preview(alpha=192)
camera.framerate = 24
camera.start_recording('/home/pi/myvideo.h264')
camera.wait_recording(15)

camera.stop_recording()
camera.stop_preview()
