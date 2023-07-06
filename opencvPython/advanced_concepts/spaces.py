import os
import random

import cv2 as cv
import matplotlib.pyplot as plt


def resize_image(image, scale=0.75):
    return cv.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)), interpolation=cv.INTER_AREA)


photos = os.listdir("./animal_photos")
# img = cv.imread(f"./animal_photos/{photos[random.randint(0, len(photos) - 1)]}")
img = resize_image(cv.imread(f"./animal_photos/{photos[0]}"), 0.2)
cv.imshow("Original", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to LAB / L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
BGR = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV ---> BGR", BGR)

# LAB to BGR
BGR = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("Lab ---> BGR", BGR)

cv.waitKey(0)
