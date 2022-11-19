import cv2

cap = cv2.VideoCapture("101_640x360.mp4")

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Relaxing Bird", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow("Relaxing Bird")

cap.release()