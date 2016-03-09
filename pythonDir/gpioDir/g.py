#!/usr/bin/python

import time
import os
import RPi.GPIO as GPIO

INPUT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

while True: 
	if (GPIO.input(INPUT_PIN) == True):
		print('3.3 #########################################################################')
	else:
		print('0')
	time.sleep(0.01)
