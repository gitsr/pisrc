#!/usr/bin/python

import os
import sys
import time
import rrdtool
import calendar
import RPi.GPIO as GPIO

# Read electricity meter which flashes every 1Wh consumed
# We'll store the data as Joules to remove the time component
# W = J/s so 1Wh = 3600J, so every flash is 3600J consumed

JoulesInWh = 3600

INPUT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

lastEpoch = calendar.timegm(time.gmtime())
up = False

def saveit(val):
  with open( "last.counter", "w" ) as f:
    print >> f, val

def readit():
  with open( "last.counter", "r" ) as f:
    val = f.read()
    return int(val)

joules = int(readit())
print "start from %s joules" % joules

while True: 
  if (GPIO.input(INPUT_PIN) == True):
    if (up is False):
      joules = joules + JoulesInWh
      epoch = calendar.timegm(time.gmtime())
      if epoch > (lastEpoch + 60):
        print "rrd", epoch, " ", joules
        saveit(joules)
        rrdtool.update("./elec.rrd", "--template", "joules", "%s:%s" % (epoch,joules))
        lastEpoch = epoch
    up = True
  else:
    if (up is True):
      up = False

  time.sleep(0.01)
