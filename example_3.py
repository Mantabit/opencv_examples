import cv2 as cv
import numpy as np

img = cv.imread('test.png',0)
ret,img=cv.threshold(img,150,255,0)

#find the contour of the object
img2,contours,hierarchy=cv.findContours(img,1,2)
cnt=contours[0]
M=cv.moments(cnt)
#plot the complete contour
contour_full=np.reshape(cnt,(cnt.shape[0],2))
img_fullcontour=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
cv.drawContours(img_fullcontour,[contour_full],0,(0,0,255),2)
cv.imshow("Full Contour",img_fullcontour)
#compute the minimum rectangle and plot it
rect=cv.minAreaRect(cnt)
box=np.int0(cv.boxPoints(rect))
img_minrect=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
cv.drawContours(img_minrect,[box],0,(0,0,255),2)
cv.imshow("Minimum Rectangle",img_minrect)