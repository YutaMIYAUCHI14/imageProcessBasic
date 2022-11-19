import cv2
import matplotlib.pyplot as plt

img = cv2.imread("valorant_logo_design.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = imgGray.shape

Imin = 255
Imax = 0
Isum = 0
Iave = 0.0

for y in range(height):
    for x in range(width):
        value = imgGray[y,x]

        if value > Imax:
            Imax = value
        if value < Imin:
            Imin = value
        Isum += value
Iave = Isum/(width*height)

print("Imin = " + str(Imin))
print("Imax = " + str(Imax))
print("Iave = " + str(Iave))

histogram = cv2.calcHist([imgGray], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
histogram.shape
plt.plot(histogram)
plt.show()