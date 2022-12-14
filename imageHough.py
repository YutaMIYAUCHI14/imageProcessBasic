import cv2
import numpy as np

img = cv2.imread('road.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,300)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=80,maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("Image",img)
cv2.imshow("Edges",edges)

key = cv2.waitKey(0)

cv2.destroyWindow("Image")
cv2.destroyWindow("Edges")
