import cv2
import numpy as np
img = cv2.imread('frame_193.png')
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##kernal = np.ones((5, 5),np.uint8)
##out = cv2.erode(img,kernal,iterations=1)
##output = cv2.dilate(img,kernal,iterations=1)
output1 = cv2.Canny(img,100,225)
ret,thresh = cv2.threshold(img1,120,255,cv2.THRESH_BINARY)
##print(out)
##print(output)
cv2.imshow('windowwww',output1)
cv2.imshow('windowww1w',thresh)
cv2.imshow('windows',img)
##cv2.imshow('window',out)
##cv2.imshow('windowss',output)

cv2.waitKey(0)
cv2.destroyAllWindows()
