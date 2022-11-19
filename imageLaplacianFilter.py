import cv2
import numpy as np

img = cv2.imread("valorant_logo_design.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgGray = cv2.Laplacian(imgGray, -1)

cv2.imwrite("valorant_logo_design_laplacian.jpg", imgGray)