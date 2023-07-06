import cv2 as cv
import numpy as np
import os


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


def rotate(img, angle, rot_point=None):
    (h, w) = img.shape[:2]

    if rot_point is None:
        rot_point = (w // 2, h // 2)

    rot_matrix = cv.getRotationMatrix2D(rot_point, angle, 1.0)

    return cv.warpAffine(img, rot_matrix, (w, h))


images = os.listdir("./animal_photos/")

cropped = cv.imread("./animal_photos/" + images[4])[350:-1000, 200:-200]
img = resize_frame(cropped, 0.21)

cv.imshow("eagle", img)

blank1 = np.zeros(img.shape[:2], dtype="uint8")

rectangle_mask = cv.rectangle(blank1, (img.shape[1] // 8, img.shape[0] // 8),
                              (img.shape[1] // 8 * 7, img.shape[0] // 8 * 7), 255, -1)

custom_mask = rectangle_mask

for i in range(30):
    custom_mask = cv.bitwise_or(custom_mask, rotate(custom_mask, 12))

cv.imshow("custom_masked", cv.bitwise_and(img, img, mask=custom_mask))

cv.waitKey(0)
