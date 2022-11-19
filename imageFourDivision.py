import cv2
import numpy as np

img=cv2.imread("mandrill.jpg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray=hsv[:,:,2]

gray=gray/64
gray=gray.astype("uint8")*64

cv2.imshow("image",img)
cv2.imshow("gray_4color",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
