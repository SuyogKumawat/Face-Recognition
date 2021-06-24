import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pywhatkit

def emailtoany(sender,receiver):
    fromaddr = sender
    toaddr = receiver
   
# instance of MIMEMultipart
    msg = MIMEMultipart()
  
# storing the senders email address  
    msg['From'] = fromaddr
  
# storing the receivers email address 
    msg['To'] = toaddr
  
# storing the subject 
    msg['Subject'] = "Alert Face Detected Check Now!!"
  
# string to store the body of the mail
    body = "Download the image from attachment mentioned below"
  
# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
# open the file to be sent 
    filename = "img.jpg"
    attachment = open("C:\\Users\\hp\\Desktop\\summerintern\\Computer Vision\\task6\\img.jpg", "rb")
  
# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
  
# To change the payload into encoded form
    p.set_payload((attachment).read())
  
# encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
# attach the instance 'p' to instance 'msg'
    msg.attach(p)
  
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
    s.starttls()
  
# Authentication
    s.login(fromaddr, "task6done@")
  
# Converts the Multipart msg into a string
    text = msg.as_string()
  
# sending the mail
    s.sendmail(fromaddr, toaddr, text)
  
# terminating the session
    s.quit()

#print(emailtoany("hrsample777@gmail.com","suyogkumawat1999@gmail.com"))


def watsapptoany(mob_no,time_inhour,time_inmin):
    pywhatkit.sendwhatmsg(mob_no, 'Alert:Face Detected',time_inhour,time_inmin)