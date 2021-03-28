import cv2
import numpy as np
import time
import os
from PID_IMAGE import *

cam=cv2.VideoCapture(0)#Start webcam capture
c = None

#os.system ('sudo rmmod uvcvideo')
#os.system ('sudo modprobe uvcvideo quirks=2')

while(1):
    ret0,frame =cam.read()                          #Start webcam capture Frame  
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Set gray balance rang
    ret1, thresh = cv2.threshold(imgray,48,255,cv2.THRESH_BINARY_INV)                #Set gray balance range, this converts the image to WHITE / BLACK
    contorno, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]#Identify contour in black / white image
    
    vi=70  #Initial velocity
    
    if len(contorno) > 0:  #Draw center point of contour
        c = max(contorno, key=cv2.contourArea)
        M = cv2.moments(c)        
        cx = int(M["m10"]/M["m00"])
        cy = int(M["m01"]/M["m00"])        
        cv2.circle(frame, (cx,cy),13,(2,250,250),-1)

    height, width  = frame.shape[:2]
    middleX = int(width/2) #Get the coordinate center X
    middleY = int(height/2)#Get the coordinate center Y
            
    cv2.drawContours(frame,c,-1,(0,255,0),3)              #Draw the contour in Green
    cv2.circle(frame,(middleX,middleY), 10, (0,0,255), -1)#Draw the center circle of the image,RED
    
    error=cx-middleX      #Get error
    Kp= (100-vi)/middleX  #Generate Kp value from the initial speed
    
    PID(error,Kp,0.012,0.0167,vi) #Call Module for PID Control
        
    #cv2.imshow('camera1',frame)
    #cv2.imshow('camera2',thresh1)
    #cv2.imshow('camera3',thresh2)
    key=cv2.waitKey(1) & 0xFF
