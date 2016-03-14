#!/usr/bin/env python

import re
import cgi
import time
import rrdtool
import datetime
from datetime import timedelta

def graphit( st, en ):
  rrdtool.graph("../elec/tmp.png",
               '--imgformat', 'PNG',
               '--width', '900',
               '--height', '240',
               '--start', str(st),
               '--end', str(et),
               '--right-axis', '1:0',
               '--vertical-label', 'Watts',
               '--lower-limit', '0',
               'DEF:watts=/var/elec/elec.rrd:joules:AVERAGE',
               'CDEF:totaljoules=watts,%d,*' % (et-st),
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

def parseTime( t ):

  pattern = "%Y-%m-%d %H:%M:%S"

  if "now" == t:
    ret = (datetime.datetime.now()).strftime(pattern)
  else:
    m = re.search( "([-]?\d+)([mhdw])", t )
    if m:
      digit = int(m.group(1))
      period = m.group(2)
      if "m" == period:
        delta = digit * timedelta(minutes=1)
      elif "h" == period:
        delta = digit * timedelta(hours=1)
      elif "d" == period:
        delta = digit * timedelta(hours=24)
      elif "w" == period:
        delta = digit * timedelta(days=7)

      ret = (datetime.datetime.now() + delta).strftime(pattern)
    else:
      ret = t

  return int(time.mktime(time.strptime(ret, pattern)))


print "Content-Type: text/html\n"
print """<html><head/><body>"""

form = cgi.FieldStorage()
initST = form.getvalue('startTime')
initET = form.getvalue('endTime')

if not initST:
  initST = "-1h"
  initET = "now"

print """
<form action="m.py" method="GET">
<input name="startTime" value="%s">
<input name="endTime" value="%s">
<input type="submit" value="Submit"> 
</form>""" %( initST, initET )

print """<p>Enter absolute "2016-03-14 06:00:00", or relative "-2h", "now" terms</p>"""

st = parseTime( initST )
et = parseTime( initET )

if st and et:
  graphit(st,et)
  print """<img src="../elec/tmp.png" alt="tmp" />"""
else:
  print "<p>no pic</p>"

print """</body></html>"""
