import picamera

camera = picamera.PiCamera()

camera.resolution = (200,200)

camera.capture('testimage.jpg')
