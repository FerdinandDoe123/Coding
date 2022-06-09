from tkinter import N
import cv2
from numpy import rec

cam = cv2.VideoCapture(0)
cam.set(3, 660)
cam.set(4, 500)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retv, frame = cam.read()
    warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(warna, 1.3, 5)

    for (x, y, h, w) in faces :
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,225,63), 2)
        rec_muka = warna [y : y + h, x : x + w]
        cv2.imshow('WEBCAM', frame)
        close = cv2.waitKey(1) & 0xFF
        if close == 27 or close == ord ('n') :
            break


cam.release()
cv2.destroyAllWindows()
