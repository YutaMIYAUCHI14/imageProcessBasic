import cv2

img = cv2.imread("valorant_logo_design.jpg")

cv2.namedWindow("Valorant Logo Design", cv2.WINDOW_NORMAL)
cv2.imshow("Valorant Logo Design", img)
cv2.waitKey(0)
cv2.destroyWindow("Valorant Logo Design")