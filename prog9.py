import cv2
from skimage.feature import local_binary_pattern

import numpy as np


image=cv2.imread("rv.jpg")

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray_image,100,300)
lbp=local_binary_pattern(gray_image,24,3,method="uniform")


lbp=np.uint8((lbp/np.max(lbp))*150)


cv2.imshow("original image",image)
cv2.imshow("edges",edges)
cv2.imshow("texture (lbp)",lbp)

cv2.waitKey(0)

cv2.destroyAllWindows()