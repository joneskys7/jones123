#very long program
#it should take 16 images and stepper motor should turn one complete rotation.
#download this code in raspberry pi using the following commands in raspberry pi:

#cd Desktop
#git clone https://github.com/joneskys7/cam.git
#cd cam
#sudo python stepcam.py

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import time
import picamera
from time import sleep
camera = picamera.PiCamera()
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

j=0
def jonny(j):
    i = j 
    j = "image%s.jpg"%(i)
    i = i+1
    return j

for a in range (16):
    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    g = jonny(j)
    j = j+1
    print g
    camera.capture(j)
    time.sleep(5)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)

    GPIO.output(8,1)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)
		
    GPIO.output(8,0)
    GPIO.output(18,1)
    GPIO.output(22,0)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,1)
    GPIO.output(23,0)
    time.sleep(0.006)

    GPIO.output(8,0)
    GPIO.output(18,0)
    GPIO.output(22,0)
    GPIO.output(23,1)
    time.sleep(0.006)
GPIO.cleanup()
