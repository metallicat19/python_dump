import cv2 as cv
import os


def read_image_from_folder(path: str = "./faces/", element: int = 0):
    images = os.listdir(path)
    return cv.imread(path + images[element])


def resize_frame(frame, scale=0.75):
    return cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)


img = resize_frame(read_image_from_folder(element=0))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("./haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

print(f"number of faces: {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("person", img)
cv.imshow("gray_person", gray)
cv.waitKey(0)
cv.destroyAllWindows()
