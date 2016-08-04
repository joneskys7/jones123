
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

while True:
	if GPIO.input(3)==1:
		GPIO.output(23,0)
		print " 1 up"
		time.sleep(0.1)   
	elif GPIO.input(5)==1:
                GPIO.output(23,1)
		print " 1 down"
		time.sleep(0.1)   
	elif GPIO.input(7)==1:
                GPIO.output(23,0)
		print " 2 up "
		time.sleep(0.1)
	elif GPIO.input(8)==1:
                GPIO.output(23,1)
		print " 2 down"
		time.sleep(0.1)
	elif GPIO.input(10)==1:
                GPIO.output(23,0)
		print " 3 up"
		time.sleep(0.1)
	elif GPIO.input(11)==1:
                GPIO.output(23,1)
		print " 3 down "
		time.sleep(0.1)   
	elif GPIO.input(12)==1:
                GPIO.output(23,0)
		print " 4 up "
		time.sleep(0.1)
	elif GPIO.input(13)==1:
                GPIO.output(23,1)
		print " 4 down "
		time.sleep(0.1)
	elif GPIO.input(15)==1:
                GPIO.output(23,0)
		print " 5 up "
		time.sleep(0.1)
	elif GPIO.input(16)==1:
                GPIO.output(23,1)
		print " 5 down "
		time.sleep(0.1)
	else:
                GPIO.output(23,1)
		print " all off"

		
GPIO.cleanup()    
