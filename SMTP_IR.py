import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
GPIO.setup(7,GPIO.IN)
while True:
    if GPIO.input(7)==1:
        msg = MIMEMultipart()
        msg['From'] = 'dummymai007@gmail.com'
        msg['To'] = 'ksjones777@gmail.com'
        msg['Subject'] = 'MOTION DETECTION'
        message = 'SOMEBODY IS STANDING INFRONT OF UR GATE'
        msg.attach(MIMEText(message))

        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login('dummymai007@gmail.com', 'dummymai007123')

        mailserver.sendmail('dummymai007@gmail.com','ksjones777@gmail.com',msg.as_string())

        mailserver.quit()
        print("sent")
    else:
        print("invalid")
