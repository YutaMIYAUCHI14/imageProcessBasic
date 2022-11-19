import cv2

cap = cv2.VideoCapture("101_640x360.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fmt = cv2.VideoWriter_fourcc("m","p","4","v")
writer = cv2.VideoWriter("birdRelaxingGray.mp4", fmt, fps, (width, height), 0)

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Bird Relaxing Gray Scale", frameGray)
    writer.write(frameGray)

cap.release()
writer.release()
cv2.destroyAllWindows()