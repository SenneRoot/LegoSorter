#import picamera

class Camera:
	def __init__(camera):
		camera = picamera.PiCamera()
		camera.resolution = (1920, 1080)

<<<<<<< HEAD
    def takeSnapshot(camera):
        camera.capture('image.jpg')
        print("Snapshot captured")
=======
	def takeSnapshot(self):
        	camera.capture('image.jpg')
        	print("Snapshot captured")
>>>>>>> b40d9881354efa53b07a1614b355014c9de62baf
