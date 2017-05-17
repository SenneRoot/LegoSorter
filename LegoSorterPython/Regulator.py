from Vibrating_Funnel import Vibrating_Funnel
from Conveyor_Belt import Conveyor_Belt
from Camera import Camera

import picamera
import Regulator

class Regulator:
    def __init__(self):
        self.Regulator = Regulator

    #def determineColour(self, Snapshot):

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
