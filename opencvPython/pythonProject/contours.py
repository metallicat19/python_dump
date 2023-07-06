import cv2 as cv
import numpy as np


def resizeFrame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


img = resizeFrame(cv.imread("Screenshots/Screenshot (21).png"))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

"""blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)"""

ret, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found")

cv.waitKey(0)
