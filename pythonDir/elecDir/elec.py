#!/usr/bin/python

# resolutions
# 1 day @ 1 minute, 4 weeks @ 5 minute, 2 years @ 1 hour
#
# rrdtool create elec.rrd --start 0 --step=60 \
# DS:joules:COUNTER:6000:U:U \
# RRA:AVERAGE:0.5:1:60       \
# RRA:AVERAGE:0.5:5:8064     \
# RRA:AVERAGE:0.5:60:17520

import os
import sys
import time
import rrdtool
import calendar
import RPi.GPIO as GPIO
from collections import defaultdict

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
  with open( "/var/elec/last.counter", "w" ) as f:
    print >> f, val

def readit():
  with open( "/var/elec/last.counter", "r" ) as f:
    val = f.read()
    return int(val)

def graphit():
  now = calendar.timegm(time.gmtime())
  endTime = now
  oneDayAgo = now - ( 24 * 60 * 60 )

  startDataTime = 1456612500

  d = ({'last_1h' : [now - (60 * 60),            now],
        'last_1d' : [now - (24 * 60 * 60),       now],
        'last_1w' : [now - (7  * 24 * 60 * 60),  now],
        'last_1m' : [now - (30 * 24 * 60 * 60),  now],
        'last_1y' : [now - (365 * 24 * 60 * 60), now],
        })

  for k,v in d.iteritems():
    rrdtool.graph("/var/www/elec/%s.png" % k,
                 '--imgformat', 'PNG',
                 '--width', '740',
                 '--height', '140',
                 '--start', str(max(v[0],startDataTime)),
                 '--end', str(v[1]),
                 '--vertical-label', 'Watts',
                 '--right-axis', '1:0',
                 '--lower-limit', '0',
                 'DEF:watts=/var/elec/elec.rrd:joules:AVERAGE',
                 'CDEF:totaljoules=watts,%d,*' % (v[1]-v[0]),
                 'CDEF:kWh=totaljoules,3600000,/',
                 'CDEF:cost=kWh,0.115,*',
                 'CDEF:sh100=watts,1.00,*',
                 'CDEF:sh90=watts,0.90,*',
                 'CDEF:sh80=watts,0.80,*',
                 'CDEF:sh70=watts,0.70,*',
                 'CDEF:sh60=watts,0.60,*',
                 'CDEF:sh50=watts,0.50,*',
                 'CDEF:sh40=watts,0.40,*',
                 'CDEF:sh30=watts,0.30,*',
                 'CDEF:sh20=watts,0.20,*',
                 'CDEF:sh10=watts,0.10,*',
                 'AREA:sh100#FF0000:',
                 'AREA:sh90#FF3200:',
                 'AREA:sh80#FF0000:',
                 'AREA:sh70#FF6600:',
                 'AREA:sh60#FF9900:',
                 'AREA:sh50#FFCC00:',
                 'AREA:sh40#FFFF00:',
                 'AREA:sh30#CCFF00:',
                 'AREA:sh20#99FF00:',
                 'AREA:sh10#65FF00:',
                 'VDEF:Average=watts,AVERAGE',
                 'HRULE:Average#9595FF:Average',
                 'GPRINT:watts:AVERAGE:%5.0lf Watts\\t',
                 'GPRINT:kWh:AVERAGE:kWh %4.2lf\\t',
                 'GPRINT:cost:AVERAGE:cost %3.2lf pounds\\n')

#
# Entry Point
#
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
        rrdtool.update("/var/elec/elec.rrd", "--template", "joules", "%s:%s" % (epoch,joules))
        graphit()
        lastEpoch = epoch
    up = True
  else:
    if (up is True):
      up = False

  time.sleep(0.01)
