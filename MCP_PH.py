import RPi.GPIO as GPIO
import time
import spidev
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.IN)
spi = spidev.SpiDev()
spi.open(0,0)
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
count=0
signal = 0
for i in range(100):
    signal = ReadChannel(signal)
    print "--------------------------------------------"
    print("signal value: {}".format(signal))
    time.sleep(0.1)
    
    if(signal>=560 and signal<=580):
        print "acid"
        time.sleep(0.8)
   
    elif (signal>=603 and signal<=630):
        print "water"
        time.sleep(0.8)
    
    else:
        print "Base"
        time.sleep(0.8)
    
    
GPIO.cleanup()
