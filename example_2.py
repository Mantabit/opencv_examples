import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while(True):
    #read the next frame
    ret,frame=cap.read()
    #convert the image to grayscale
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #check if end of video
    if not ret:
        break
    #display the resulting image
    cv.imshow("frame",gray)
    #wait for 1ms
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()