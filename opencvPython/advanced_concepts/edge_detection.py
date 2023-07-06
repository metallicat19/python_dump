import cv2 as cv
import numpy as np
import os


def read_image_from_folder(path: str = "./animal_photos/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


img = read_image_from_folder(element=8)[1600:-1200, 400:-400]
# cv.imshow("husky", resize_frame(img, scale=0.23))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayscale", resize_frame(gray, scale=0.23))

bone = read_image_from_folder("./Fractured Bone/", element=0)
# cv.imshow("fractured", bone)

gray_bone = cv.cvtColor(bone, cv.COLOR_BGR2GRAY)
# cv.imshow("grayscale", gray_bone)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", resize_frame(lap, scale=0.23))

lap_bone = cv.Laplacian(gray_bone, cv.CV_64F)
lap = np.uint8(np.absolute(lap_bone))
# cv.imshow("laplacian edge", lap_bone)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("sobel x", resize_frame(sobelx, scale=0.23))
cv.imshow("sobel y", resize_frame(sobely, scale=0.23))
cv.imshow("combined", resize_frame(combined_sobel, scale=0.23))

# canny
canny = cv.Canny(gray, 254, 255)
cv.imshow("canny", resize_frame(canny, scale=0.23))

cv.waitKey(0)
cv.destroyAllWindows()
