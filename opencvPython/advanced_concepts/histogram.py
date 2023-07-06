import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os


def resize_image(image, scale):
    return cv.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)), interpolation=cv.INTER_AREA)


def read_image_from_folder(path: str = "./animal_photos/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


image = read_image_from_folder("./animal_photos/", element=6)
cv.imshow("Image", resize_image(image, 0.2))

blank1 = np.zeros((image.shape[:2]), dtype="uint8")
blank2 = np.zeros((image.shape[:2]), dtype="uint8")

mask1 = cv.circle(blank1, (blank1.shape[1] // 2 + 150, blank1.shape[0] // 2 + 150), 900, 255, -1)
mask2 = cv.circle(blank2, (blank2.shape[1] // 2 + 150, blank2.shape[0] // 2 + 150), 900, 255, -1)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("masked", resize_image(cv.bitwise_and(gray, gray, mask=mask1), 0.2))

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask1, [256], [0, 256])

# plt.figure()
# plt.title("grayscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("Number of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# colour histogram

colours = ("b", "g", "r")

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")

for i, col in enumerate(colours):
    hist = cv.calcHist([image], [i], mask2, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.imshow("gray", resize_image(gray, 0.2))
cv.waitKey(0)
