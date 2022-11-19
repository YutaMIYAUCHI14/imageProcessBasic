import cv2

img = cv2.imread("valorant_logo_design.jpg")

bValo = img[:,:,0]
gValo = img[:,:,1]
rValo = img[:,:,2]

imgGray = bValo*0.1 + gValo*0.6 + rValo*0.3

cv2.namedWindow("Valornt Logo Design Gray Scale Version", cv2.WINDOW_NORMAL)
cv2.imshow("Valornt Logo Design Gray Scale Version", imgGray.astype("uint8"))
cv2.waitKey(0)
cv2.destroyWindow("Valornt Logo Design Gray Scale Version")