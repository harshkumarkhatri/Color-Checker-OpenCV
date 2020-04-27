import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background=0
while(1):

    # Take each frame
    _, frame = cap.read()
    frame=np.flip(frame,axis=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    # print(lower_blue)
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_all=cv2.morphologyEx(mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask)
    

    # Bitwise-AND mask and original image
    streamA = cv2.bitwise_and(frame,frame, mask= mask2)
    # streamB = cv2.bitwise_and(background, background, mask = mask)
    # output=cv2.addWeighted(streamA,1,streamB,1,0)

    # print(streamA)
    # for i in streamA:
    #     for j in i:
    #         if j[0]<130 and j[0]>110:
    #             print("True") 
    # print(streamA)
    points = cv2.findNonZero(mask)
    avg = np.mean(points, axis=0)
    print(points)
    # print(avg)
    cv2.rectangle(streamA,(points[0][0][0],points[0][0][1]),(700,700),(255,0,0),2)
    cv2.imshow('frame',streamA)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()