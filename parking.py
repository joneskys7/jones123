#CONNECTIONS;
#Connect IR sensor 1 to  15
#Connect IR sensor 2 to  13
#Connect IR sensor 3 to  7
#RED LED 1 TO 23
#GREEN LED 1 TO 29
#RED LED 2 TO 31
#GREEN LED 2 TO 33
#RED LED 3 TO 35
#GREEN LED 3 TO 37

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(23,GPIO.OUT) #RED1
GPIO.setup(29,GPIO.OUT) 
GPIO.setup(31,GPIO.OUT)  #RED2
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)  #RED3
GPIO.setup(37,GPIO.OUT)

import time
while True:
    if GPIO.input(15)==1:
        print("a is full")
        GPIO.output(23,1)
        GPIO.output(29,0)
        if GPIO.input(13)==1:
            print("b is full")
            GPIO.output(31,1)
            GPIO.output(33,0)
            if GPIO.input(7)==1:
                print("c is full")
                GPIO.output(35,1)
                GPIO.output(37,0)
            elif GPIO.input(7)==0:
                print("c is empty")
                GPIO.output(35,0)
                GPIO.output(37,1)
        elif GPIO.input(13)==0:
            print("b is empty")
            GPIO.output(31,0)
            GPIO.output(33,1)
            if GPIO.input(7)==1:
                print("c is full")
                GPIO.output(35,1)
                GPIO.output(37,0)
            elif GPIO.input(7)==0:
                print("c is empty")
                GPIO.output(35,0)
                GPIO.output(37,1)
        
    elif GPIO.input(15)==0:
        print("a is empty")
        GPIO.output(23,0)
        GPIO.output(29,1)
        if GPIO.input(13)==1:
            print("b is full")
            GPIO.output(31,1)
            GPIO.output(33,0)
            if GPIO.input(7)==1:
                print("c is full")
                GPIO.output(35,1)
                GPIO.output(37,0)
            elif GPIO.input(7)==0:
                print("c is empty")
                GPIO.output(35,0)
                GPIO.output(37,1)
        elif GPIO.input(13)==0:
            print("b is empty")
            GPIO.output(35,0)
            GPIO.output(37,1)
            if GPIO.input(7)==1:
                print("c is full")
                GPIO.output(35,1)
                GPIO.output(37,0)
            elif GPIO.input(7)==0:
                print("c is empty")
                GPIO.output(35,0)
                GPIO.output(37,1)
    print("----------------------------------------------")
    time.sleep(2)

GPIO.cleanup()    
                        
                        
                    
    
    
    
