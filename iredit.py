import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.OUT)
while True:
	if GPIO.input(7)==1:
           GPIO.output(8,True)
	   print "ON"
    	   time.sleep(1)	
	elif GPIO.input(7)==0:
           GPIO.output(8,False)
	   print "OFF"
	   time.sleep(1)
GPIO.cleanup()
