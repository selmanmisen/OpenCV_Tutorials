import cv2 as cv
import numpy as np

img = cv.imread('fotograflar/shapes2.jpg')
font=cv.FONT_HERSHEY_COMPLEX

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

x,threshold= cv.threshold(gray,150,255,cv.THRESH_BINARY)
contours,k= cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

maxArea=0
for i in contours:

    area = round(cv.contourArea(i))
    perimeter= round(cv.arcLength(i,True))
    
    
    if maxArea<area:
        maxArea=area


    moments=cv.moments(i)
    if moments['m00'] != 0:
        mx=int(moments["m10"]/moments["m00"])
        my=int(moments["m01"]/moments["m00"])
    else:
        mx,my=0,0
    
    
    
    epsilon= 0.01*cv.arcLength(i,True)
    approx= cv.approxPolyDP(i,epsilon,True)
    cv.drawContours(img,[approx],0,(0,100,200),1)

    x=approx.ravel()[0]
    y=approx.ravel()[1]
    
    if len(approx)==3:
        cv.putText(img,"ucgen",(x-10,y-10),font,0.75,1)
    elif len(approx)==4:
        cv.putText(img,"dortgen",(x-10,y-10),font,0.75,1)
    elif len(approx)==5:
        cv.putText(img,"besgen",(x-10,y-10),font,0.75,1)
    elif len(approx)==6:
        cv.putText(img,"altigen",(x-10,y-10),font,0.75,1)
    else:
        cv.putText(img,"cember",(x-10,y-10),font,0.75,1)

    if maxArea != area:
        cv.putText(img,"G",(mx,my),font,0.75,1)
        cv.putText(img,f"Alan:{area}",(x+10,y+25),font,0.5,(0,0,0))
        cv.putText(img,f"Cevre:{perimeter}",(x+10,y+50),font,0.5,(0,0,0))
        
    print(len(approx))
   
cv.imshow('gray',gray)
cv.imshow('img',img)
cv.waitKey(0)