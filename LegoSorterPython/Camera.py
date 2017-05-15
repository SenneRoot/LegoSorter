import picamera

class Camera:
	def __init__():
		camera = picamera.PiCamera()
		camera.resolution = (1920, 1080)

	def takeSnapshot():
        	camera.capture('image.jpg')
        	print("Snapshot captured")
