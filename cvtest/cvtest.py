import cv2
import time
print(cv2.__version__)
cam = cv2.VideoCapture(0)

if not cam.isOpened():
	print('카메라 오픈 에러')
	exit()
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#트랙바 세팅
cv2.namedWindow('aa')
def nothing(x):
    pass

# Blur 커널 크기 :1~31 홀수 아닌 경우 +1 처리)
cv2.createTrackbar('Blur', 'aa', 7, 31, nothing)
# Threshold 임계값: 0~255
cv2.createTrackbar('Thresh', 'aa', 120, 255, nothing)

while cv2.waitKey(1) != 27:
    ret, frame = cam.read()
    
    #트랙바 값 읽기
    k = cv2.getTrackbarPos('Blur', 'aa')
    t = cv2.getTrackbarPos('Thresh', 'aa')
    
    c1 =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Gray 변환
    
    # c2: Blur 
    if k % 2 == 0:
        k += 1
    c2 =cv2.GaussianBlur(frame,(k,k), 0)	# Blur 효과
    
    # c3 : threshold
    _, c3 = cv2.threshold(c2, t, 255, cv2.THRESH_BINARY) # 임계 효과
       
    cv2.imshow('aa',frame)
    cv2.imshow('bb',c1)
    cv2.imshow('cc',c2)
    cv2.imshow('cc',c3)
    
cv2.imwrite('c1.jpg',frame)
cv2.waitKey()
cv2.destroyAllWindows()



