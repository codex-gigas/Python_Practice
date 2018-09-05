import cv2
import numpy as np
img1 = cv2.imread('frame_193.png')
img2 = cv2.imread('frame_42.png')
##img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
##img4 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
alpha = 0.5
beta = 1-alpha
gamma = 0
img5 = cv2.addWeighted(img1,alpha,img2,beta,gamma)
img6 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
output1 = cv2.Canny(img5,100,225)
ret,thresh = cv2.threshold(img5,120,255,cv2.THRESH_BINARY)
ret1,thresh1 = cv2.threshold(img6,120,255,cv2.THRESH_BINARY)

cv2.imshow('Edge detector',output1)
cv2.imshow('Binary_image',thresh)
cv2.imshow('Alpha_Blending',img5)
cv2.imshow('Binary_Convert_to_GrayScale',thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
