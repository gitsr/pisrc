#!/usr/bin/python

import os
import sys
import time
import rrdtool
import calendar
from collections import defaultdict

now = calendar.timegm(time.gmtime())
endTime = now
oneDayAgo = now - ( 24 * 60 * 60 )

d = ({'last_1h' : [now - (60 * 60),            now],
      'last_1d' : [now - (24 * 60 * 60),       now],
      'last_1m' : [now - (30 * 24 * 60 * 60),  now],
      'last_1y' : [now - (365 * 24 * 60 * 60), now] })

for k,v in d.iteritems():
  rrdtool.graphv("/var/www/elec/%s.png" % k,
               '--imgformat', 'PNG',
               '--width', '740',
               '--height', '140',
               '--start', str(v[0]),
               '--end', str(v[1]),
               '--vertical-label', 'Watts',
               '--title', '30 Park Rd, Electricity Usage %s' % k,
               '--lower-limit', '0',
               'DEF:watts=/var/elec/elec.rrd:joules:AVERAGE',
               'CDEF:totaljoules=watts,%d,*' % (v[1]-v[0]),
               'CDEF:kWh=totaljoules,3600000,/',
               'CDEF:cost=kWh,0.1,*',
               'VDEF:MM=watts,MAXIMUM',
               'CDEF:s10=watts,150,LT,watts,150,IF',
               'CDEF:s20=watts,300,LT,watts,300,IF',
               'CDEF:s30=watts,450,LT,watts,450,IF',
               'CDEF:s40=watts,800,LT,watts,800,IF',
               'CDEF:s50=watts,1500,LT,watts,1500,IF',
               'CDEF:s60=watts,3000,LT,watts,3000,IF',
               'CDEF:s70=watts',
               'CDEF:sh10=s10,MM,LT,watts,MM,IF',
               'CDEF:sh20=s20,MM,LT,watts,MM,IF',
               'CDEF:sh30=s30,MM,LT,watts,MM,IF',
               'CDEF:sh40=s40,MM,LT,watts,MM,IF',
               'CDEF:sh50=s50,MM,LT,watts,MM,IF',
               'CDEF:sh60=s60,MM,LT,watts,MM,IF',
               'CDEF:sh70=s70,MM,LE,watts,MM,IF',
               'AREA:sh70#FF0000:',
               'AREA:sh60#FF9900:',
               'AREA:sh50#FFCC00:',
               'AREA:sh40#FFFF00:',
               'AREA:sh30#CCFF00:',
               'AREA:sh20#99FF00:',
               'AREA:sh10#65FF00:',
               'VDEF:Average=watts,AVERAGE',
               'HRULE:Average#9595FF:Average',
               'GPRINT:watts:AVERAGE:Power %4.0lf Watts\\t',
               'GPRINT:kWh:AVERAGE:kWh %4.2lf\\t',
               'GPRINT:cost:AVERAGE:Cost %3.2lf\\n')
