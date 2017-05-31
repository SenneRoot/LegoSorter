from enum import Enum
from Colour import Colour

import time

class Lego_Sorter():
    def pushLego(self, Colour):
	if(Colour == Colour.Red):
		print ("Red Lego is pushed!")
	elif(Colour == Colour.Green):
                print ("Green Lego is pushed!")
	elif(Colour == Colour.Blue):
		print ("Blue Lego is pushed!")
	elif(Colour == Colour.Yellow):
		print ("Yellow Lego is pushed")
	elif(Colour == Colour.Else):
		print ("Trash!")

