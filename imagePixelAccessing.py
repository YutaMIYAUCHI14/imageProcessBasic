import cv2

img = cv2.imread("valorant_logo_design.jpg")

print(img[30,50]) # img[y,x] ... 点(x,y)の画素[B,G,R]
print(type(img[30,50]))
print(img[30,50,0])
print(img[0:30,0:50]) # (0,0) ~ (50,30)を対角とする画素の範囲