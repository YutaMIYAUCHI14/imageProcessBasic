import cv2

img = cv2.imread("valorant_logo_design.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Valorant Logo Design Gray Scale Version", cv2.WINDOW_NORMAL)
cv2.imshow("Valorant Logo Design Gray Scale Version", imgHSV[:,:,2])
cv2.waitKey(0)
cv2.destroyWindow("Valorant Logo Design Gray Scale Version")