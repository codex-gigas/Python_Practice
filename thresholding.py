import cv2
import numpy as np

img = cv2.imread('4.2.07.tiff')

a = np.array([0,225,0])
b = np.array([0,255,0])

thresh = cv2.inRange(img,a,b)

cv2.imshow('win1',img)
cv2.imshow('win2',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
