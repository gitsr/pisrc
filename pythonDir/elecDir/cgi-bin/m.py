#!/usr/bin/env python

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
               'GPRINT:watts:AVERAGE:Avg Power %6.0lf Watts\\t',
               'GPRINT:kWh:AVERAGE:kWh %4.2lf\\t',
               'GPRINT:cost:AVERAGE:cost %3.2lf pounds\\n')

print "Content-Type: text/html\n"
print """<html><head/><body>"""

onemin = timedelta(minutes=1)
pattern = "%Y-%m-%d %H:%M:%S"

form = cgi.FieldStorage()
initST = form.getvalue('startTime')
initET = form.getvalue('endTime')

if not initST:
  n = datetime.datetime.now()
  initST = (n-(10*onemin)).strftime(pattern)
  initET = n.strftime(pattern)

print """
<form action="m.py" method="GET">
<input name="startTime" value="%s">
<input name="endTime" value="%s">
<input type="submit" value="Submit"> 
</form>""" %( initST, initET )

st = int(time.mktime(time.strptime(initST, pattern)))
et = int(time.mktime(time.strptime(initET, pattern)))

if st and et:
  graphit(st,et)
  print """<img src="../elec/tmp.png" alt="tmp" />"""
else:
  print "<p>no pic</p>"

print """</body></html>"""
