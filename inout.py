import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(11,GPIO.IN)
COUNT=0
IN=0
while True:
    if GPIO.input(3)==0:
        time.sleep(1)
        if GPIO.input(11)==1:
            COUNT=COUNT+1
            IN=IN+1
            print("welcome")
            print("total count",COUNT)
            print("people inside",IN)
            time.sleep(2)
            
    elif GPIO.input(11)==1:
        time.sleep(1)
        if GPIO.input(3)==0:
            IN=IN-1
            print("out")
            print("total count",COUNT)
            print("people inside",IN)
            time.sleep(2)
            

