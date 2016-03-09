#!/usr/bin/python

import time
import os
import RPi.GPIO as GPIO

INPUT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

while True:
  channel = GPIO.wait_for_edge(INPUT_PIN, GPIO.BOTH,1000)
  if channel is None:
    print('Timeout occurred')
  else:
    print('Edge detected on channel', channel)
