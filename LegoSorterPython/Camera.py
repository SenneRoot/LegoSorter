import Camera
import picamera

class Camera:
	def __init__(self):
		self.Camera = picamera.PiCamera()
		self.Camera.resolution = (1920, 1080)
		#self.Snapshot = None

	def takeSnapshot(self):
        	Camera.capture('image.jpg')
        	print("Snapshot captured")
