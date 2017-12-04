import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
pins=[8,18,22,23]
for p in pins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p,False)
while True:
    if GPIO.input(7)==1:
        seq=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        print ('OPEN')
        for p1 in range(512):
                for halfstep in range(4):
                        for p1 in range(4):
                                GPIO.output(pins[p1],seq[halfstep][p1])
                                time.sleep(0.001)
                                
                                if GPIO.input(7)==1:
                                    time.sleep(10)
                                    if GPIO.input(7)==1:
                                        time.sleep(10)
                                    else:
                                        seq=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
                                        print ('CLOSE')
                                        for p1 in range(512):
                                                for halfstep in range(4):
                                                        for p1 in range(4):
                                                                GPIO.output(pins[p1],seq[halfstep][p1])
                                                                time.sleep(0.001)
                                else:
                                    seq=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
                                    print ('CLOSE')
                                    for p1 in range(512):
                                            for halfstep in range(4):
                                                    for p1 in range(4):
                                                            GPIO.output(pins[p1],seq[halfstep][p1])
                                                            time.sleep(0.001)
        
        
    else:
        
    print("----------------------------------------------")
    time.sleep(2)

GPIO.cleanup()    
                        
                        
                    
    
    
    
