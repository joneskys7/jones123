import GPIO.RPi as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,OUTPUT)
while True:
	GPIO.output(7,1)
	print("LED ON")
	time.sleep(1)
	GPIO.output(7,0)
	print("LED OFF")
	time.sleep(1)
GPIO.cleanup()