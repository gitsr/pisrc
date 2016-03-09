#!/usr/bin/env python

import cgi
import matplotlib.pyplot as plt

print "Content-Type: text/html\n"
print """<html><head/><body>"""

print """<p>hi</p>
<form action="m.py" method="GET">
<input name="os" value="linux">
<input type="submit" value="Submit"> 
</form>"""


form = cgi.FieldStorage()
v = form.getvalue('os')

if v:
  plt.plot([1,2,3,4,2,6,3,7,6,4,3,2])
  plt.ylabel('some numbers')
  plt.savefig("g.png")
  print "<p>hello %s</p>" % v
  print """<img src="../g.png" alt="g" />"""
else:
  print "<p>no pic</p>"

print """</body></html>"""
