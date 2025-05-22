import cv2


s_img = cv2.imread("c1.jpg")
#g_img =cv2.GaussianBlur(s_img,(7,7), 0)
r,cimg = cv2.threshold(s_img, 120, 255, cv2.THRESH_BINARY)

c_img - cv2.Canny(s_image, 120, 100, 300)

cv2.imshow("",s_img)
cv2.imshow("Converted",g_img)
cv2.waitKey(0)
