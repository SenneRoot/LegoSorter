from Camera import Camera															#Importeer Camera
from Lego_Sorter import Lego_Sorter													#Importeer Lego_Sorter, de klasse die de solenoids aanstuurt
from Colour import Colour															#Importeer de enumeration Colour
from picamera.array import PiRGBArray												#Importeer PiRGBArray om het datatype framearrays te kunnen gebruiken

import thread																		#Importeer thread om threads te kunnen starten
import atexit																		#Importeer atexit om een goede afhandeling te kunnen verzorgen bij het afsluiten van het programma
import time																			#Importeer time om de sleep() functie te kunnen gebruiken
from picamera import PiCamera														#Importeer PiCamera om de aangesloten camera te kunnen gebruiken
import Regulator																	#Importeer een instantie van eigen klasse, dit wordt gebruikt 
import cv2																			#Importeer cv2 om gebruik te kunnen maken van OpenCV
import numpy as np																	#Importeer numpy
import RPi.GPIO as GPIO																#Importeer RPi.GPIO om de GPIO pins aan te kunnen sturen
import enum as Enum																	#Importeer Enum om de enumeration uit de klasse 'Colour' te kunnen gebruiken

lower_range_rood = np.array([169, 100, 100], dtype=np.uint8)
upper_range_rood = np.array([189, 255, 255], dtype=np.uint8)

lower_range_geel = np.array([15, 100, 100], dtype=np.uint8)
upper_range_geel = np.array([35, 255, 255], dtype=np.uint8)

lower_range_blauw = np.array([95, 100, 100], dtype=np.uint8)
upper_range_blauw = np.array([115, 255, 255], dtype=np.uint8)

lower_range_groen = np.array([64, 100, 100], dtype=np.uint8)
upper_range_groen = np.array([84, 255, 255], dtype=np.uint8)

class Regulator:																	#Maak de klasse 'Regulator' aan
    def __init__(self):																#Constructor die de GPIO mode naar BCM zet en de benodigde GPIO pins configureerd als output
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)
    
    def getImage(self, camera):														#Functie voor het maken van een foto met de camera
        camera.capture('image.jpg')
        print("Snapshot captured!")
    
    def exit_handler():																#Exit afhandeler die er voor zorgt dat de GPIO pins op laag worden gezet op het moment dat het programma wordt afgesloten
	GPIO.cleanup()

    atexit.register(exit_handler)

    def determineColour(image):
	def get_img():
		img = image
		return img
		
	def find_color(hsv):
		if cv2.inRange(hsv, lower_range_rood, upper_range_rood).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Red))		#Start een nieuwe thread die de functie pushLego() start, die in de klasse 'Lego_Sorter' staat met de parameter Colour.Red
		elif cv2.inRange(hsv, lower_range_geel, upper_range_geel).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Yellow))	#Start een nieuwe thread die de functie pushLego() start, die in de klasse 'Lego_Sorter' staat met de parameter Colour.Yellow
		elif cv2.inRange(hsv, lower_range_blauw, upper_range_blauw).any():	
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Blue))		#Start een nieuwe thread die de functie pushLego() start, die in de klasse 'Lego_Sorter' staat met de parameter Colour.Blue
		elif cv2.inRange(hsv, lower_range_groen, upper_range_groen).any():
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Green))	#Start een nieuwe thread die de functie pushLego() start, die in de klasse 'Lego_Sorter' staat met de parameter Colour.Green
		else:
			thread.start_new_thread(Lego_Sorter.pushLego, (Lego_Sorter(), Colour.Else))		#Start een nieuwe thread die de functie pushLego() start, die in de klasse 'Lego_Sorter' staat met de parameter Colour.Else

	def to_hsv(img):
		hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
		return hsv
	
	hsv = to_hsv(image)
	find_color(hsv)

    if __name__ == "__main__":															#Main van het programma
	__init__(Regulator)																	#Activeer __init__(), de constructor met een instantie van Regulator als parameter
	camera = PiCamera()																	#Maak een instantie van PiCamera aan
        camera.resolution = (100, 150)													#Zet de resolutie van de camera naar 100 bij 150 pixels, dit is voldoende voor het herkennen van een Lego blokje
	camera.framerate = 20																#Zet de framerate van de camera naar 20 frames per seconde, 
	rawCapture = PiRGBArray(camera)														#Maak een instatie van PiRGBArray en geef 'camera' mee als parameter, een instantie van PiCamera
	time.sleep(0.1)																		#Wacht 100 milliseconden
	for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True): #Laat de camera frames opnemen
		image = frame.array																#Zet een frame van de videostream in 'image'
		determineColour(image)															#Activeer de beeldherkenning en geef 'image', een frame van de videostream mee als parameter
		key = cv2.waitKey(1) & 0xFF														#Zorgt er voor dat de videostream stopgezet wordt als het programma afgesloten wordt
		rawCapture.truncate(0)
		if key == ord("q"):
			break
