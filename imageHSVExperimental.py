from tkinter import image_names
import cv2

img = cv2.imread("valorant_logo_design.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

imgHSV[:,:,1] = 255

imgAns = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)

cv2.namedWindow("Valorant Logo Design Experiment", cv2.WINDOW_NORMAL)
cv2.imshow("Valorant Logo Design Experiment", imgAns)
cv2.waitKey(0)
cv2.destroyWindow("Valorant Logo Design Experiment")