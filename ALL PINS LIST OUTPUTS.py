import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
opins=[3,5,6,7,8,10,11,12,13,14,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40]
for p in opins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p,False)
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p,False)
