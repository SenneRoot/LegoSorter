from Vibrating_Funnel import Vibrating_Funnel
from Conveyor_Belt import Conveyor_Belt
from Camera import Camera
from Lego_Sorter import Lego_Sorter
from Colour import Colour
from picamera.array import PiRGBArray

import thread
import atexit
import time
from picamera import PiCamera
import Regulator
import cv2
import numpy as np
import RPi.GPIO as GPIO
import enum as Enum

lower_range_rood = np.array([169, 100, 100], dtype=np.uint8)
upper_range_rood = np.array([189, 255, 255], dtype=np.uint8)

lower_range_geel = np.array([15, 100, 100], dtype=np.uint8)
upper_range_geel = np.array([35, 255, 255], dtype=np.uint8)

lower_range_blauw = np.array([95, 100, 100], dtype=np.uint8)
upper_range_blauw = np.array([115, 255, 255], dtype=np.uint8)

lower_range_groen = np.array([64, 100, 100], dtype=np.uint8)
upper_range_groen = np.array([84, 255, 255], dtype=np.uint8)

class Regulator:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)

    def runConveyorBelt(self):
        belt1 = Conveyor_Belt()
        belt2 = Conveyor_Belt()
        belt3 = Conveyor_Belt()
        Conveyor_Belt.twistConveyorBelt(belt1)
        Conveyor_Belt.twistConveyorBelt(belt2)
        Conveyor_Belt.twistConveyorBelt(belt3)

    def runVibratingFunnel(self, vibrating_funnel):
        vibrating_funnel.vibrateFunnel()

    def get_colour():
	return currentColour
    
    def getImage(self, camera):
        camera.capture('image.jpg')
        print("Snapshot captured!")
    
    def exit_handler():
	GPIO.cleanup()

    atexit.register(exit_handler)

    def determineColour(image):
	def get_img():
		img = image
		return img
	def find_color(hsv):
		if cv2.inRange(hsv, lower_range_rood, upper_range_rood).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Red))
		elif cv2.inRange(hsv, lower_range_geel, upper_range_geel).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Yellow))
		elif cv2.inRange(hsv, lower_range_blauw, upper_range_blauw).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Blue))
		elif cv2.inRange(hsv, lower_range_groen, upper_range_groen).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Green))
		else:
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Else))

	def to_hsv(img):
		hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
		return hsv
	
	#img = get_img()
	hsv = to_hsv(image)
	find_color(hsv)

    if __name__ == "__main__":
	__init__(Regulator)
	camera = PiCamera()
        camera.resolution = (200, 200)
	camera.framerate = 20
	rawCapture = PiRGBArray(camera)
	time.sleep(0.1)
	runVibratingFunnel(Regulator, Vibrating_Funnel())
        runConveyorBelt(Regulator)
	for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
		image = frame.array
		determineColour(image)
		#cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0xFF
		rawCapture.truncate(0)
		if key == ord("q"):
			break
	#image = getImage(Regulator, camera)
	#determineColour(image)	
        #while True:
		#ret, frame = camera.read()
        	#image = getImage(Regulator, camera)
	#	determineColour(frame)
		#thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Green))
