import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("valorant_logo_design.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.title("original")
plt.imshow(imgRGB)

k = 18
kernel = np.array([[-k/9, -k/9, -k/9], [-k/9, 1+8*k/9, -k/9], [-k/9, -k/9, -k/9]])
imgSharpRGB = cv2.filter2D(imgRGB, ddepth = -1, kernel = kernel)
imgSharp = cv2.cvtColor(imgSharpRGB, cv2.COLOR_RGB2BGR)

plt.subplot(1,2,2)
plt.title("sharpening")
plt.imshow(imgSharpRGB)

plt.show()

cv2.imwrite("valorant_logo_design.jpg", img)
cv2.imwrite("valorant_logo_design_sharpening.jpg", imgSharp)