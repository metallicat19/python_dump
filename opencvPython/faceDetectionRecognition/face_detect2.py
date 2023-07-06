import cv2 as cv
import os


def read_image_from_folder(path: str = "./faces/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)


def changeRes(w, h):

