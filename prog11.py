import cv2
img=cv2.imread("rv.jpg")
contours,_=cv2.findContours(cv2.Canny(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),30,200),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0,1))
cv2.imshow("contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
