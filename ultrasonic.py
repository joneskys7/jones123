import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.IN)  
GPIO.setup(7,GPIO.OUT)

while True:
	if GPIO.input(11)==0:
		start=time.time()
		time.sleep(1)
	elif GPIO.input(11)==1:
		stop=time.time()
		elapsed=stop-start
 		distance=elapsed*170
		print "distance of an object:",distance
GPIO.cleanup()    
