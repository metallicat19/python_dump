import cv2 as cv
import os


def read_image_from_folder(path: str = "./animal_photos/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


img = resize_frame(read_image_from_folder("./animal_photos/", element=7), scale=0.12)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow("inverse thresh", thresh_inv)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow("adaptive threshold", adaptive_thresh)

bone = resize_frame(read_image_from_folder("./Fractured Bone/", element=0), scale=1.25)
gray_bone = cv.cvtColor(bone, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray_bone, 100, 225, cv.THRESH_BINARY)
cv.imshow("bone fracture", thresh)

adaptive_thresh = cv.adaptiveThreshold(gray_bone, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 5)
cv.imshow("adaptive threshold", adaptive_thresh)

cv.imshow("bone", bone)
cv.waitKey(5000)
