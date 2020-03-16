import time
import cv2


def pic():

    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)
    return_value, image = camera.read()
    cv2.imwrite("camera.png", image)
    del(camera)