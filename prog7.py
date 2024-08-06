import cv2
image=cv2.imread("rv.jpg")

h,w=image.shape[:2]

cv2.imshow("upper left",image[:h//2,:w//2])
cv2.imshow("upper right",image[:h//2,w//2:])
cv2.imshow("lower left",image[h//2:,:w//2])
cv2.imshow("lower right",image[h//2:,w//2:])


cv2.waitKey(0)
cv2.destroyAllWindows()