import cv2
image=cv2.imread("rv.jpg")

blur=cv2.GaussianBlur(image,(21,21),0)
median_blur =cv2.medianBlur(image,15)
bilateral=cv2.bilateralFilter(image,15,75,75)
cv2.imshow("orgiginal",image)
cv2.imshow("median_blur",median_blur)
cv2.imshow("bilateral",bilateral)
cv2.imshow("gaussina blur",blur)
cv2.waitKey(0)

cv2.destroyAllWindows()