import RPi.GPIO as GPIO 
import time 
import urllib 
import httplib 
GPIO.setmode(GPIO.BCM) 
GPIO_PIR = 7 
GPIO.setup(GPIO_PIR, GPIO.IN)  
Current_State  = 0 
Previous_State = 0 
try: 
print "PIR Module Test (CTRL+C to exit)" 
 while GPIO.input(GPIO_PIR)==1: 
  Current_State  = 0 
time.sleep(2) 
print "Ready" 
while True: 
Current_State = GPIO.input(GPIO_PIR) 
if Current_State==1 and Previous_State==0: 
    start_time=time.time() 
    print "SOME ONE IN PROXIMITY" 
    Previous_State=1 
    params =                    urllib.urlencode({'field1':Current_State,'key':'FN2V6M702FFUWXA8'}) 
        headers = {"Content-type": "application/x-www-formurlencoded","Accept":"text/plain"} 
        conn = httplib.HTTPConnection("api.thingspeak.com:80") 
        conn.request("POST", "/update", params, headers) 
        response = conn.getresponse() 
        data = response.read() 
        print response.status, response.reason 
        conn.close() 
    time.sleep(20) 
  
   elif Current_State==0 and Previous_State==1: 
          stop_time=time.time() 
    print "NO ONE IN PROXIMITY ", 
    elapsed_time=int(stop_time-start_time) 
    print " (Elapsed time : " + str(elapsed_time) + " secs)" 
    Previous_State=0 
    params =  
urllib.urlencode({'field1': Current_State,'key':'06XPH8RWI3LAX3VE'}) 
        headers = {"Content-type": "application/x-www-formurlencoded","Accept":"text/plain"} 
        conn = httplib.HTTPConnection("api.thingspeak.com:80") 
        conn.request("POST", "/update", params, headers) 
        response = conn.getresponse() 
        data = response.read() 
        print response.status, response.reason 
        conn.close() 
time.sleep(20) 
except KeyboardInterrupt: 
print "Quit" 
 GPIO.cleanup()  
