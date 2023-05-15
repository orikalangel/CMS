#
from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation=180

camera.start_preview()
sleep(52)
camera.capture('/home/st-001/Documents/1.jpg')#if "1%s.jpg %i" replace "1.jpg" that chance tha name of the file - in loop
camera.stop_preview()