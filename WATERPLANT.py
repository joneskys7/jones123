import RPi.GPIO as GPIO 
import time
from time import sleep
import os 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(7,GPIO.OUT) 
GPIO.setup(23, GPIO.IN) 
GPIO.setup(8, GPIO.IN) 
GPIO.setwarnings(False) 
state = GPIO.input(23) 
GPIO.output(7,False) 
file = open("SensorData.txt", "w") #stores data file in same directory as this program file #Define function to measure charge time  
def RC_Analog(Pin):   
	counter=0   
	start_time = time.time()  #Discharge capacitor   
	GPIO.setup(8, GPIO.OUT)   
	GPIO.output(8, GPIO.LOW)   
	time.sleep(0.1) #in seconds, suspends execution.     #Count loops until voltage across capacitor reads high on GPIO   
	while (GPIO.input(8)==GPIO.LOW):     
	counter=counter+1    
	end_time = time.time() 
	 return end_time - start_time  #Main program loop 
	 count=0  
	 if(GPIO.input(8)==1):    
		reading = RC_Analog(24) #store counts in a variable     
		print "Soil is moist" 
 		time.sleep(1) 
         else:   
		print "soil is dry"   
		time.sleep(1)   
		GPIO.output(7,1)  
		print "pump on"   
		time.sleep(2)   
		GPIO.output(7,0)   
		print "pump off"     
GPIO.cleanup()  
