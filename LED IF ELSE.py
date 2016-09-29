import RPi.GPIO as GPIO
import time  
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

while True:
        if GPIO.input(3)==0:
                GPIO.output(7,1)
                GPIO.output(8,1)
                print "on "
                
        else:
                GPIO.output(7,0)
                GPIO.output(8,0)
                print "off"

GPIO.cleanup()  
