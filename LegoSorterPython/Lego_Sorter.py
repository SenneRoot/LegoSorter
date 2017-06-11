from enum import Enum							#Importeer Enum om de meegegeven kleur te kunnen vergelijken
from Colour import Colour						#Importeer de enumeration Colour om de meegegeven kleur te kunnen vergelijken

import RPi.GPIO as GPIO
import time

class Lego_Sorter():							#Klasse die geactiveerd wordt door een thread vanuit de klasse 'Regulator'
    def pushLego(self, Colour):					#Functie die de solenoid van de bijbehorende meegegeven kleur een duwbeweging laat maken
	if(Colour == Colour.Red):					#Vergelijk de meegegven kleur met rood
		time.sleep(0.07)						#Wacht tot het rode Lego blokje bij de bijbehorende solenoid is
		GPIO.output(22, GPIO.HIGH)				#Zet de GPIO pin die met de solenoid voor de rode Lego blokjes verbonden is, op hoog
		time.sleep(0.1)							#Wacht 100 miliseconden
                GPIO.output(22, GPIO.LOW)		#Zet de GPIO pin weer op laag
		print ("Red Lego is pushed!")
	elif(Colour == Colour.Green):				#Vergelijk de meegegven kleur met groen
		time.sleep(0.22)						#Wacht tot het groene Lego blokje bij de bijbehorende solenoid is
		GPIO.output(23, GPIO.HIGH)				#Zet de GPIO pin die met de solenoid voor de groene Lego blokjes verbonden is, op hoog
		time.sleep(0.1)							#Wacht 100 miliseconden
                GPIO.output(23, GPIO.LOW)		#Zet de GPIO pin weer op laag
                print ("Green Lego is pushed!")
	elif(Colour == Colour.Blue):				#Vergelijk de meegegven kleur met blauw
		time.sleep(0.38)						#Wacht tot het blauwe Lego blokje bij de bijbehorende solenoid is
		GPIO.output(24, GPIO.HIGH)				#Zet de GPIO pin die met de solenoid voor de rode Lego blokjes verbonden is, op hoog
                time.sleep(0.1)					#Wacht 100 miliseconden
                GPIO.output(24, GPIO.LOW)		#Zet de GPIO pin weer op laag
		print ("Blue Lego is pushed!")
	elif(Colour == Colour.Yellow):				#Vergelijk de meegegven kleur met geel
		time.sleep(0.19)						#Wacht tot het gele Lego blokje bij de bijbehorende solenoid is
		GPIO.output(25, GPIO.HIGH)				#Zet de GPIO pin die met de solenoid voor de rode Lego blokjes verbonden is, op hoog
		time.sleep(0.1)							#Wacht 100 miliseconden
                GPIO.output(25, GPIO.LOW)		#Zet de GPIO pin weer op laag
		print ("Yellow Lego is pushed")
	elif(Colour == Colour.Else):				#Er wordt geen kleur herkent
		print ("Trash!")

