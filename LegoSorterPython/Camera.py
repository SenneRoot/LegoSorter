import picamera

class Camera:
	#def __init__(self):
		#self.Camera = Camera
		#self.camera.resolution = (1920, 1080)
		#self.Snapshot = None

	def takeSnapshot(self):
		camera = picamera.PiCamera()
		self.camera.resolution = (1920, 1080)
        	camera.capture('image.jpg')
        	print("Snapshot captured")
