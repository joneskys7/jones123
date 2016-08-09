import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
print "dist measurement in progress"
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.IN)

GPIO.output(3,0)
print  "waiting for sensor to settle"
time.sleep(2)
while True:
        GPIO.output(3,1)
        time.sleep(0.00001)
        GPIO.output(3,0)

        while GPIO.input(5)==0:
            pulse_start = time.time()

        while GPIO.input(5)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17150
        distance = round(distance,2)
        print "distance",distance,"cm"
        time.sleep(1)
GPIO.cleanup()


