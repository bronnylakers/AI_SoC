import cv2

s1 = cv2.imread('c1.jpg')
s2 = cv2.imread('c2.jpg')

diff = cv2.absdiff(s1, s2)

r,thre = cv2.threshold(diff, 120, 255, cv2.THRESH_BINARY)

cann = cv2.Canny(diff, 120, 200)

cont,r = cv2.findContours(thre, RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)

cv2.imshow("diff", diff)
cv2.imshow("Threshold",thre)
#cv2.imshow("Canny", cann)
for a in cont 
	x,y,w,h   = cv2.boundingRect((x,y), (x+w,y+h), (255,0,0), 2)
cv2.imshow("contours",cont)


cv2.waitKey()
