from time import sleep

import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    # video, image, live-video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# capture = cv.VideoCapture("E:/highlights/War Thunder/War Thunder 2021.08.26 - 13.56.46.12.DVR.mp4")
capture = cv.VideoCapture(0)


def changeRes(width, height):
    # live-video
    capture.set(3, width)
    capture.set(4, height)


while True:
    isTrue, frame = capture.read()

    cv.imshow("video", rescaleFrame(frame, scale=0.6))

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
