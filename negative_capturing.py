import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    img = abs(255-frame)
##    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Negative',img)
    if cv2.waitKey(1) == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()
