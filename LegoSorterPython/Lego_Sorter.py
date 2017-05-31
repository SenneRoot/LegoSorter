from enum import Enum
from Colour import Colour

import RPi.GPIO as GPIO
import time

class Lego_Sorter():
    def pushLego(self, Colour):
	if(Colour == Colour.Red):
		GPIO.output(22, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(22, GPIO.LOW)
		print ("Red Lego is pushed!")
	elif(Colour == Colour.Green):
		GPIO.output(23, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(23, GPIO.LOW)
                print ("Green Lego is pushed!")
	elif(Colour == Colour.Blue):
		GPIO.output(24, GPIO.HIGH)
                time.sleep(0.75)
                GPIO.output(24, GPIO.LOW)
		print ("Blue Lego is pushed!")
	elif(Colour == Colour.Yellow):
		GPIO.output(25, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(25, GPIO.LOW)
		print ("Yellow Lego is pushed")
	elif(Colour == Colour.Else):
		print ("Trash!")

