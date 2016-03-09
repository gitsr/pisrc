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
      'last_8h' : [now - (8 * 60 * 60),        now],
      'last_1d' : [now - (24 * 60 * 60),       now],
      'prior_1d': [oneDayAgo - (24 * 60 * 60), oneDayAgo],
      'last_1m' : [now - (30 * 24 * 60 * 60),  now],
      'last_1y' : [now - (365 * 24 * 60 * 60), now] })

for k,v in d.iteritems():
  rrdtool.graph("/var/elec/%s.png" % k,
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
               'AREA:watts#00FF00:Watts',
               'VDEF:Average=watts,AVERAGE',
               'HRULE:Average#9595FF:Average',
               'COMMENT: \\n',
               'GPRINT:watts:AVERAGE:Avg Power %6.0lf Watts\\t',
               'GPRINT:kWh:AVERAGE:kWh %4.2lf\\t',
               'GPRINT:cost:AVERAGE:cost %3.2lf pounds\\n')
