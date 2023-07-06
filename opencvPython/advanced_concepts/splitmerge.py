import cv2 as cv
import numpy as np
import os


def resize_image(image, scale=0.75):
    return cv.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)), interpolation=cv.INTER_AREA)


photos = os.listdir('./animal_photos')

img = resize_image(cv.imread(f"./animal_photos/{photos[2]}"), 0.15)
cv.imshow('Original', img)

#print(img.)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(f"blue: {b.shape}")
print(f"green: {g.shape}")
print(f"red: {r.shape}")

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(10000)
