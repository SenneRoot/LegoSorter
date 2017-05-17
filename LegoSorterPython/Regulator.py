from Vibrating_Funnel import Vibrating_Funnel
from Conveyor_Belt import Conveyor_Belt
from Camera import Camera

#import picamera
import Regulator

class Regulator:
    def __init__(self):
        self.Regulator = Regulator


    #def determineColour(self, Snapshot):

    def getImage(camera):
<<<<<<< HEAD
        Camera.takeSnapshot(Camera)
=======
        Camera.takeSnapshot(camera)
>>>>>>> b40d9881354efa53b07a1614b355014c9de62baf

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
<<<<<<< HEAD
        vibrating_funnel = Vibrating_Funnel()
        camera = Camera()
		camera = picamera.PiCamera()
        camera.resolution = (1920, 1080)
        runVibratingFunnel(vibrating_funnel)
        runConveyorBelt()
        while True:
            image = getImage(camera)
=======
        runVibratingFunnel(Regulator)
        runConveyorBelt(Regulator)
	camera = picamera.PiCamera()
       # while True:
	image = getImage(camera)
>>>>>>> b40d9881354efa53b07a1614b355014c9de62baf
            #colour = determineColour(Regulator, image)
