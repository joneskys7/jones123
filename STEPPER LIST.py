import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pins=[8,18,22,23]
for p in pins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p,False)
seq=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
print 'motor rotates in clock wise direction'
for p1 in range(512):
	for halfstep in range(4):
		for p1 in range(4):
			GPIO.output(pins[p1],seq[halfstep][p1])
			time.sleep(0.001)

seq=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
print 'Motor rotates in anti-clock wise direction'
for p1 in range(512):
	for halfstep in range(4):
		for p1 in range(4):
			GPIO.output(pins[p1],seq[halfstep][p1])
			time.sleep(0.001)
GPIO.cleanup()

	

