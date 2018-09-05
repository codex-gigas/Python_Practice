import cv2

cap = cv2.VideoCapture(0)
t=0
while True:
    ret, frame = cap.read()
    cv2.imshow("windows os", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite("frame_" + str(t) + '.png', frame)
        break
    t=t+1
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
