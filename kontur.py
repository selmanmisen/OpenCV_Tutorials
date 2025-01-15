import cv2
import numpy as np

image = cv2.imread('fotograflar/shapes.jpg')  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(image, 100, 150)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0),1)

cv2.imshow("Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
