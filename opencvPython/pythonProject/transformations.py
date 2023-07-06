import os
import cv2 as cv
import numpy as np
import random


def resizeFrame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


# translation
def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)


# -x ----> left
# -y ----> up
#  x ----> right
#  y ----> down

# rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)


screenshots = os.listdir("./Screenshots/")

img = resizeFrame(cv.imread(f"./Screenshots/{screenshots[random.randint(0, 7)]}"), 0.3)
cv.imshow("image", img)

translated = translate(img, 100, -100)
# cv.imshow("translated", translated)

rotated = rotate(translated, -45)
# cv.imshow("rotated", rotated)

# resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized", resized)

# flipping
flipped = cv.flip(img, flipCode=0)  # -1 ikisi de | 0 x'e göre simetrik | 1 y'ye göre simetrik
cv.imshow("flipped", flipped)

# cropping
cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
