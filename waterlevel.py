import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
while True:

	if GPIO.input(3)==1:
	   print "Water level is FULL"
    	   time.sleep(2)	
	elif GPIO.input(3)==0:
	   print "Water level is LESS"
	   time.sleep(2)
GPIO.cleanup()
