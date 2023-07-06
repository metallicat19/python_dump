import cv2
import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


# paint it to certain color
blank_img = np.zeros((500, 500, 3), dtype=np.uint8)
blank_img[100:200, :300] = (0, 0, 255)
cv.imshow('red', blank_img)


# draw a rectangle
blank_rect_img = np.zeros((500, 500, 3), dtype=np.uint8)
cv.rectangle(blank_rect_img, (0, 0), (blank_rect_img.shape[1] // 2, blank_rect_img.shape[0] // 2), (0, 255, 0),
             thickness=-1)
cv.imshow('green', blank_rect_img)


# draw a circle
blank_circ_img = np.zeros((500, 500, 3), dtype=np.uint8)
cv.circle(blank_circ_img, (blank_circ_img.shape[1] // 2, blank_circ_img.shape[0] // 2), radius=70, color=(0, 255, 255),
          thickness=-1)
cv.imshow('circle', blank_circ_img)

# 4 draw a line
blank_line_img = np.zeros((500, 500, 3), dtype=np.uint8)
cv.line(blank_line_img, (50, 50), (blank_line_img.shape[1] // 2, blank_line_img.shape[0] // 2), color=(255, 0, 0),
        thickness=5)
cv2.imshow("line", blank_line_img)

# write text
blank_text_img = np.zeros((500, 500, 3), dtype=np.uint8)
cv.putText(blank_text_img, "Hello", (25, 250), cv.FONT_HERSHEY_COMPLEX, 5, (255, 127, 127), 3)
cv.imshow("text", blank_text_img)

cv.waitKey(0)
