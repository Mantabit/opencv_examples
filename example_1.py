import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
ret,frame=cap.read()
height=frame.shape[0]
width=frame.shape[1]

red_pixel_bgr=np.uint8([[[0,0,255]]])
red_pixel_hsv=cv.cvtColor(red_pixel_bgr,cv.COLOR_BGR2HSV)

#define upper and lower limits for red color
lower_blue=np.uint8([110,50,50])
upper_blue=np.uint8([130,255,255])
kernel=np.ones((5,5),np.uint8)

#def getPositions(mask):
#    left=0
#    right=0
#    bottom=0
#    top=0
#    foundLeft=False
#    foundTop=False
#    for i in range(0,width):
#        col=mask[:,i]
#        if np.sum(col)!=0:
#            right=i
#            if not foundLeft:
#                left=i
#                foundLeft=True
#    for i in range(0,height):
#        row=mask[i,:]
#        if(np.sum(row)!=0):
#            bottom=i
#            if not foundTop:
#                top=i
#                foundTop=True
#    return (left,right,top,bottom)

while(True):
    #take the current frame
    ret,frame=cap.read()
    #convert bgr to hsv
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #compute the color threshold bitmask
    mask=255-cv.inRange(hsv,lower_blue,upper_blue)
    mask_erroded=cv.erode(mask,kernel,iterations=1)
#    left,right,top,bottom=getPositions(mask)
#    cv.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
    
    img,contours,hierarchy=cv.findContours(mask,1,2)
    
    if len(contours)!=0:
        cnt=contours[0]
        rect=cv.minAreaRect(cnt)
        box=np.int0(cv.boxPoints(rect))
        mask=cv.cvtColor(mask,cv.COLOR_GRAY2BGR)
        cv.drawContours(mask,[box],0,(0,0,255),2)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    
    if cv.waitKey(10) & 0xFF==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()