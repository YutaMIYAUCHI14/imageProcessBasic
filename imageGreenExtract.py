import cv2
import numpy as np

img = cv2.imread("valorant_logo_design.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

greenLow = np.array([30, 0, 0])
greenHigh = np.array([90, 255, 255])

mask = cv2.inRange(imgHSV, greenLow, greenHigh)
imgAns = cv2.bitwise_and(img, img, mask = mask)

cv2.namedWindow("Valorant Logo Design Green Extract", cv2.WINDOW_NORMAL)
cv2.imshow("Valorant Logo Design Green Extract", imgAns)
cv2.waitKey(0)
cv2.destroyWindow("Valorant Logo Design Green Extract")