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
  rrdtool.graph("./png/%s.png" % k,
               '--imgformat', 'PNG',
               '--width', '740',
               '--height', '140',
               '--start', str(v[0]),
               '--end', str(v[1]),
               '--vertical-label', 'Watts',
               '--title', '30 Park Rd, Electricity Usage %s' % k,
               '--lower-limit', '0',
               'DEF:watts=elec.rrd:joules:AVERAGE',
               'CDEF:totaljoules=watts,%d,*' % (v[1]-v[0]),
               'CDEF:kWh=totaljoules,3600000,/',
               'CDEF:cost=kWh,0.1,*',
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
               'AREA:sh100#FF0000:Watts',
               'AREA:sh90#FF3200:Watts',
               'AREA:sh80#FF0000:Watts',
               'AREA:sh70#FF6600:Watts',
               'AREA:sh60#FF9900:Watts',
               'AREA:sh50#FFCC00:Watts',
               'AREA:sh40#FFFF00:Watts',
               'AREA:sh30#CCFF00:Watts',
               'AREA:sh20#99FF00:Watts',
               'AREA:sh10#65FF00:Watts',
               'VDEF:Average=watts,AVERAGE',
               'HRULE:Average#9595FF:Average',
               'COMMENT: \\n',
               'GPRINT:watts:AVERAGE:Avg Power %6.0lf Watts\\t',
               'GPRINT:kWh:AVERAGE:kWh %4.2lf\\t',
               'GPRINT:cost:AVERAGE:cost %3.2lf pounds\\n')
