import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt


def read_image_from_folder(path: str = "./animal_photos/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


img = read_image_from_folder(element=9)

(H, W) = img.shape[:2]
print(H, W)