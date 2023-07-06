import cv2 as cv
import numpy as np
import os


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


images = os.listdir("./animal_photos/")

cropped = cv.imread("./animal_photos/" + images[4])[350:-1000, 200:-200]
img = resize_frame(cropped, 0.21)

cv.imshow("eagle", img)

blank1 = np.zeros(img.shape[:2], dtype="uint8")
blank2 = np.zeros(img.shape[:2], dtype="uint8")

circle_mask = cv.circle(blank1, (img.shape[1] // 2, img.shape[0] // 2), 200, 255, -1)

rectangle_mask = cv.rectangle(blank2, (img.shape[1] // 8, img.shape[0] // 8),
                              (img.shape[1] // 8 * 7, img.shape[0] // 8 * 7), 255, -1)

masked = cv.bitwise_and(img, img, mask=rectangle_mask)

cv.imshow("masked", masked)

cv.waitKey(7500)
