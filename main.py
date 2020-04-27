import numpy as np
import cv2



cap=cv2.VideoCapture(0)

lower_red = np.array([-10, 50, 50])
upper_red = np.array([20, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])
lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 128])

while(True):
    ret,frame=cap.read()
    frame=cv2.GaussianBlur(frame,(11,11),0)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lower_green,upper_green)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()