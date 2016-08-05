import RPi.GPIO as GPIO
import time
start=0
stop=0
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.IN)  
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

while True:
	if GPIO.input(11)==0:
		GPIO.output(8,0)
		GPIO.output(18,0)
		GPIO.output(22,0)
		GPIO.output(23,0)
		time.sleep(1)   
	elif GPIO.input(11)==1:
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
