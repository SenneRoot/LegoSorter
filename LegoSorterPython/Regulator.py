from Vibrating_Funnel import Vibrating_Funnel
from Conveyor_Belt import Conveyor_Belt
from Camera import Camera
import Regulator
from enum import Enum

class Regulator:
    def __init__(self):
        self.Regulator = Regulator

    def determineColour(self, Snapshot):

    def getImage(self):
       Camera.takeSnapshot(Camera())

    def runConveyorBelt(self):
        belt1 = Conveyor_Belt()
        belt2 = Conveyor_Belt()
        belt3 = Conveyor_Belt()
        Conveyor_Belt.twistConveyorBelt(belt1)
        Conveyor_Belt.twistConveyorBelt(belt2)
        Conveyor_Belt.twistConveyorBelt(belt3)

    def runVibratingFunnel(self):
        Vibrating_Funnel.vibrateFunnel(Vibrating_Funnel())

    if __name__ == "__main__":
        runVibratingFunnel(Regulator)
        runConveyorBelt(Regulator)
        while True:
            image = getImage(Regulator)
            colour = determineColour(Regulator, image)
