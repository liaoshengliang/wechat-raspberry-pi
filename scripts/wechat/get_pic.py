#zhtebfawtkxejgga
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import cv2

def get_pic():
    cap=cv2.VideoCapture(0)
    if cap.isOpened()==0:
        print('camera is not opened correctly!')
        cap=cv2.VideoCapture(1)
    start = time.time()
    while 1:
    
        ret,frame = cap.read()
        end = time.time()
        if end-start>=1:

             cv2.imwrite("/home/pi/scripts/wechat/result.jpg",frame)
             cap.release()
             break

