import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(21,GPIO.OUT) #RED1
GPIO.setup(29,GPIO.OUT) 
GPIO.setup(31,GPIO.OUT)  #RED2
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)  #RED3
GPIO.setup(37,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
import time
while True:
    if (GPIO.input(15)==0 and GPIO.input(16)==0 and GPIO.input(7)==0):
        GPIO.output(21,0)
        GPIO.output(29,1)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,0)
        GPIO.output(37,1)
        print("1")
        GPIO.output(13,1)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print("A-EMPTY B-EMPTY C-EMPTY")
    elif (GPIO.input(15)==0 and GPIO.input(16)==0 and GPIO.input(7)==1):
        GPIO.output(21,0)
        GPIO.output(29,1)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,1)
        GPIO.output(37,0)
        print("1")
        GPIO.output(13,1)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print("A-EMPTY B-EMPTY C-FULL")
        
    elif (GPIO.input(15)==0 and GPIO.input(16)==1 and GPIO.input(7)==0):
        GPIO.output(21,0)
        GPIO.output(29,1)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,0)
        GPIO.output(37,1)
        print("1")
        GPIO.output(13,1)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print("A-EMPTY B-FULL C-EMPTY")
    elif (GPIO.input(15)==0 and GPIO.input(16)==1 and GPIO.input(7)==1):
        GPIO.output(21,0)
        GPIO.output(29,1)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,1)
        GPIO.output(37,0)
        print("1")
        GPIO.output(13,1)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print("A-EMPTY B-FULL C-FULL")
    elif (GPIO.input(15)==1 and GPIO.input(16)==0 and GPIO.input(7)==0):
        GPIO.output(21,1)
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,0)
        GPIO.output(37,1)
        print("2")
        GPIO.output(13,0)
        GPIO.output(8,1)
        GPIO.output(10,0)
        print("A-FULL B-EMPTY C-EMPTY")
        
    elif (GPIO.input(15)==1 and GPIO.input(16)==0 and GPIO.input(7)==1):
        GPIO.output(21,1)
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,1)
        GPIO.output(37,0)
        print("2")
        GPIO.output(13,0)
        GPIO.output(8,1)
        GPIO.output(10,0)
        print("A-FULL B-EMPTY C-FULL")
    elif (GPIO.input(15)==1 and GPIO.input(16)==1 and GPIO.input(7)==0):
        GPIO.output(21,1)
        GPIO.output(29,0)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,0)
        GPIO.output(37,1)
        print("3")
        GPIO.output(13,0)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print("A-FULL B-FULL C-EMPTY")        
    elif (GPIO.input(15)==1 and GPIO.input(16)==1 and GPIO.input(7)==1):
        GPIO.output(21,1)
        GPIO.output(29,0)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,1)
        GPIO.output(37,0)
        print("A-FULL B-FULL C-FULL")
    time.sleep(1)
GPIO.cleanup()
