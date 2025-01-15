import cv2 as cv

img = cv.imread('fotograflar/fil.jpg')
cv.imshow('fil',img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

canny=cv.Canny(img,150,175)
cv.imshow('canny',canny)



cv.waitKey(0)