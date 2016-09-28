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
gas_channel = 0
for i in range(1000):
    gas_level = ReadChannel(gas_channel)
    print "--------------------------------------------"
    print("signa: {}".format(gas_level))
    time.sleep(0.1)
GPIO.cleanup()
