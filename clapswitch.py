import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
value=2
while True:
    def off():
        print("off")
        GPIO.output(11,1)
        global value
        value=0
        time.sleep(0.1)
    def on():
        print("on")
        GPIO.output(11,0)
        global value
        value=1
        time.sleep(0.1)
    
    
    if GPIO.input(3)==0:
        if value ==0:
            print (value)
            on()
        elif value ==1:
            print (value)
            off()
        else:
            global value
            on()
    
