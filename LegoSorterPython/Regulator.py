from Vibrating_Funnel import Vibrating_Funnel
from Conveyor_Belt import Conveyor_Belt
from Camera import Camera

import picamera
import Regulator
import cv2
import numpy as np

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
        self.Regulator = Regulator

    def determineColour(self, img):
		def get_img():
			import picamera
			img = cv2.imread("image.jpg", 1)
			return img
		def find_color(hsv):
			if cv2.inRange(hsv, lower_range_rood, upper_range_rood).any():
				print("dit is rood")
			elif cv2.inRange(hsv, lower_range_geel, upper_range_geel).any():
				print("dit is geel")
			elif cv2.inRange(hsv, lower_range_blauw, upper_range_blauw).any():
				print("dit is blauw")
			elif cv2.inRange(hsv, lower_range_groen, upper_range_groen).any():
				print("dit is groen")
			else:
				print("ik weet niet man")
			
		def to_hsv(img):
			hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			return hsv

		img = get_img()
		hsv = to_hsv(img)
		find_color(hsv)

	def getImage(camera):
        camera.capture('image.jpg')
		print("Snapshot captured!")

    def runConveyorBelt():
        belt1 = Conveyor_Belt()
        belt2 = Conveyor_Belt()
        belt3 = Conveyor_Belt()
        Conveyor_Belt.twistConveyorBelt(belt1)
        Conveyor_Belt.twistConveyorBelt(belt2)
        Conveyor_Belt.twistConveyorBelt(belt3)

    def runVibratingFunnel(vibrating_funnel):
        Vibrating_Funnel.vibrateFunnel(vibrating_funnel)

    if __name__ == "__main__":
        vibrating_funnel = Vibrating_Funnel()
	camera = picamera.PiCamera()
        camera.resolution = (200, 200)
        runVibratingFunnel(vibrating_funnel)
        runConveyorBelt()
        while True:
            image = getImage(camera)
