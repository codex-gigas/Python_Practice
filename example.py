import cv2

path='T:\Opencv tutorials\pictures\\'
image=path+'lena_color_512.tif'
img1=cv2.imread(image)
print(img1.shape)
cv2.imshow('battleship',img1)
if cv2.waitKey(1)==ord('q'):
    destroyAllWindows()
