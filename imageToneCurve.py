import cv2

img = cv2.imread("valorant_logo_design.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = imgGray.shape

for y in range(height):
    for x in range(width):
        val = imgGray[y,x]

        # 折れ線型トーンカーブ
        if val < 128:
            val = val*2
        else:
            val = 255
        if val > 255:
            val = 255
        if val < 0:
            val = 0
        
        imgGray[y,x] = val

cv2.imwrite("valorant_logo_design_tone_curve.jpg", imgGray)