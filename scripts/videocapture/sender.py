#zhtebfawtkxejgga
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import cv2

cap=cv2.VideoCapture(1)
if cap.isOpened()==0:
    print('camera is not opened correctly!')
    cap=cv2.VideoCapture(0)
start = time.time()
while 1:
    
    ret,frame = cap.read()
    end = time.time()
    if end-start>=2:

         cv2.imwrite("/home/pi/scripts/videocapture/result.jpg",frame)
         cap.release()
         break
def send_email(smtp_host, smtp_port, sendAddr, password, recipientAddrs, subject='', content=''):
    '''
    :param smtp_host: 
    :param smtp_port: 
    :param sendAddr: 
    :param password: 
    :param recipientAddrs: 
    :param subject: 
    :param content: 
    :return: 
    '''
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
 
 
    part = MIMEApplication(open(r'/home/pi/scripts/videocapture/result.jpg', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="result.jpg")  
    msg.attach(part)
 
    try:
        smtpSSLClient = smtplib.SMTP_SSL(smtp_host, smtp_port)  
        loginRes = smtpSSLClient.login(sendAddr, password)  
        print(f"登录结果：loginRes = {loginRes}")  # loginRes = (235, b'Authentication successful')
        if loginRes and loginRes[0] == 235:
            print(f"登录成功，code = {loginRes[0]}")
            smtpSSLClient.sendmail(sendAddr, recipientAddrs, str(msg))
            print("mail has been send successfully.")
            smtpSSLClient.quit()
        else:
            print(f"登陆失败，code = {loginRes[0]}")
    except Exception as e:
        print(f"发送失败，Exception: e={e}")
 
 
try:
    subject = 'RaspberryPi VideoCapture'
    content = '***照片拍于'+time.strftime('%Y/%m/%d %H:%M:%S')+'***\n'
    send_email('smtp.qq.com', 465, '********@qq.com', 'ffxodrrutdzhbbig', '********@qq.com', subject, content)
except Exception as err:
    print(err)
