import cv2
import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (200, 200)

while True:
	camera.capture('image.jpg')
	image = cv2.imread("image.jpg")
	time.sleep(0.5)
	color = image[100, 100]
	print color
	c = cv2.waitKey(7) % 0x100
        if c == 27 or c == 10:
        	break
