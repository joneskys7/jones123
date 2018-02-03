import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.OUT)
p=GPIO.PWM(7,50)
p.start(7.5)
while True:
    if GPIO.input(3)==0:
        print ("FULL")
        time.sleep(1)
        if GPIO.input(3)==0:
            msg = MIMEMultipart()
            msg['From'] = 'dummymai007@gmail.com'
            msg['To'] = 'kysjones@outlook.com'
            msg['Subject'] = 'BIN ALERT'
            message = 'BIN IS FULL'
            msg.attach(MIMEText(message))

            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
            mailserver.login('dummymai007@gmail.com', 'dummymai007123')

            mailserver.sendmail('dummymai007@gmail.com','kysjones@outlook.com',msg.as_string())

            mailserver.quit()
            print("sent")
            time.sleep(1)
            exit()
    	   
    elif GPIO.input(3)==1:
        print ("PLEASE USE ME")
        time.sleep(0.2)
        if GPIO.input(5)==1:
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            print ("OPEN")
        elif GPIO.input(5)==0:
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            print ("CLOSE")
           
GPIO.cleanup()
