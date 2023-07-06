import os
import cv2 as cv
import numpy as np


def resize_frame(image, scale=0.75):
    return cv.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)), interpolation=cv.INTER_AREA)


photos = os.listdir('./animal_photos')

img = resize_frame(cv.imread(f"./animal_photos/{photos[3]}"), 0.3)
cv.imshow("img", img)

# averaging = orta piksel etrafındaki(kernel size'a göre) pixellerin yoğunluğunae göre ortalama alır
average = cv.blur(img, (7, 7))
cv.imshow("average blur", average)

# gaussian blur = orta pikesel etrafındaki(kernel size'a göre) pixellerin ağırlıklı ortalamasını alır
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("gaussian blur", gaussian)

# median blur = """"" ortalama almak yerine meydanını alır
median = cv.medianBlur(img, 7)
cv.imshow("median blur", median)

# bilateral blur = normal blurleyerek gürültüyü azaltır ve kenarlarları yok etmez
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral blur", bilateral)

cv.waitKey(5000)
