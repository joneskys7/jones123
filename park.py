import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(7,GPIO.IN)
import time
while True:
    if GPIO.input(15)==1:
        print("a is full")
        if GPIO.input(13)==1:
            print("b is full")
            if GPIO.input(7)==1:
                print("c is full")
            elif GPIO.input(7)==0:
                print("c is empty")
        elif GPIO.input(13)==0:
            print("b is empty")
            if GPIO.input(7)==1:
                print("c is full")
            elif GPIO.input(7)==0:
                print("c is empty")
        
    elif GPIO.input(15)==0:
        print("a is empty")
        if GPIO.input(13)==1:
            print("b is full")
            if GPIO.input(7)==1:
                print("c is full")
            elif GPIO.input(7)==0:
                print("c is empty")
        elif GPIO.input(13)==0:
            print("b is empty")
            if GPIO.input(7)==1:
                print("c is full")
            elif GPIO.input(7)==0:
                print("c is empty")
    print("----------------------------------------------")
    time.sleep(2)

GPIO.cleanup()    
                        
                        
                    
    
    
    
