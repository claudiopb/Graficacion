import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(100,90,200),2)

cv.rectangle(img,(400,0),(500,128),(0,255,0),3)

cv.circle(img,(250,80), 75, (0,0,255), -1)



cv.ellipse(img,(100,300),(50,30),0,60,360,255,-1)

pts = np.array([[30,5],[35,30],[70,5],[50,10]], np.int32)
pts = pts.reshape((4,1,2))
cv.polylines(img,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,100), 0, 2,(255,0,255),4,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,130), 1, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,160), 2, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,190), 3, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,220), 4, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,250), 5, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,280), 6, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'OpenCV',(10,310), 7, 1,(255,255,255),2,cv.LINE_AA)

cv.imshow('Lienzo',img)

cv.waitKey(0)
cv.destroyAllWindows()
