import cv2
import numpy as np
import picamera

camera = picamera.PiCamera()

camera.capture('image.jpg')
img = cv2.imread("image.jpg", 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range_rood = np.array([169, 100, 100], dtype=np.uint8)
upper_range_rood = np.array([189, 255, 255], dtype=np.uint8)

lower_range_geel = np.array([15, 100, 100], dtype=np.uint8)
upper_range_geel = np.array([35, 255, 255], dtype=np.uint8)

if cv2.inRange(hsv, lower_range_rood, upper_range_rood).any():
    print("dit is rood")
elif cv2.inRange(hsv, lower_range_geel, upper_range_geel).any():
    print("dit is geel")
else:
    print("ik weet niet man")

cv2.imshow('image', img)

while (1):
    k = cv2.waitKey(0)
    if (k == 27):
        break

cv2.destroyAllWindows()