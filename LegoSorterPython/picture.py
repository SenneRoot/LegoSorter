import picamera

camera = picamera.PiCamera()

camera.resolution = (200,150)

camera.capture('testimage.jpg')
