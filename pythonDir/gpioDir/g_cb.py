#!/usr/bin/python

import time
import os
import RPi.GPIO as GPIO

INPUT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

def cb(channel):
  print('Edge detected on channel %s' % channel)

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH,callback=cb)
time.sleep(60);
