import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

lower_ = np.array([100,50,50])
upper_ = np.array([130,255,255])


while True:
    rep,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv,lower_,upper_)
    filtered_color=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('hsv',hsv)
    cv.imshow('masked',mask) 
    cv.imshow('filtered',filtered_color) 


    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv.destroyAllWindows()
