import cv2 as cv





"""img = cv.imread("./photos/minimalism-plane-ot.jpg")

cv.imshow("img", img)

cv.waitKey(0)"""

capture = cv.VideoCapture("E:/highlights/War Thunder/War Thunder 2021.08.26 - 13.56.46.12.DVR.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
