import cv2
import numpy as np

##def pixel_value(event,a,b,flags,param):
##    if event == cv2.EVENT_LBUTTONDBLCLK:
##        print str(x) + ', ' + str(y)
##        print img[y][x]

def main():
    path = 'T:\Opencv tutorials\pictures\\'
    image = path + 'woman_blonde.tif'
    img = cv2.imread(image)
##    cv2.namedWindow('image')
##    cv2.setMouseCallback('image', pixel_value)

#scaling
##    output = cv2.resize(img, None, fx=2, fy=2)

#Translation
##    rows, cols, dim = img.shape
##    M=np.float32([[1,0,100],[0,1,50]])
##    output = cv2.warpAffine(img,M,(cols+50,rows+100))

#Rotation
    rows, cols, dim = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
    output = cv2.warpAffine(img,M,(cols,rows))


    cv2.imshow('image', output)
    if cv2.waitKey(1)== ord('q'):
        cv2.destroyWindow('image')
if __name__=='__main__':
    main()
