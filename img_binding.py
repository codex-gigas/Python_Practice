import cv2

img1=cv2.imread('frame_42.png')
img2=cv2.imread('frame_193.png')

alpha=0.5
beta=1-alpha
gamma=0

output = cv2.addWeighted(img1,alpha,img2,beta,gamma)

cv2.imshow('window',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
