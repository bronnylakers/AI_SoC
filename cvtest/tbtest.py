import cv2

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(1) != 27:
    ret, frame = cam.read()

    cv2.imshow("mycamera", frame)

cv2.imwrite('c2.jpg',frame)
cv2.waitKey()
cv2.destroyAllWindows()
