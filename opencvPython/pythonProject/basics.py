import cv2 as cv
import numpy as np


def resize_frame(frame, scale=0.5):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


img = resize_frame(cv.imread("Fractured Bone/F14.jpg"), scale=5)
cv.imshow("image", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# edge cascade
canny = cv.Canny(img, 45, 170)
cv.imshow("canny", canny)

# dilating
dilate = cv.dilate(canny, (11, 11), iterations=5)
cv.imshow("dilate", dilate)

# eroding (reverses dilate)
eroded = cv.erode(dilate, (5, 5), iterations=2)
cv.imshow("eroded", eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# cropping
cropped = img[10:200, 200:500]
cv.imshow("cropped", cropped)

cv.waitKey(7500)
