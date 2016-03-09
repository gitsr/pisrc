#!/usr/bin/env python

import cgi
import io
import numpy as np

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['timezone'] = 'US/Eastern'
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Read the data file
data = np.genfromtxt( 'test.dat', delimiter=',' )
dates = matplotlib.dates.epoch2num(data[:,0])
tempdata = data[:,1]

# Set up the plot
fig, ax = plt.subplots(figsize=(6,5))
ax.plot_date( dates, tempdata, ls='-', color='red' )
ax.xaxis.set_major_formatter( DateFormatter( '%m/%d/%y %H:%M' ) )

# Read the number of hours argument and set xlim
arg = cgi.FieldStorage()
try:
    h = int( arg.getvalue('hrs', '-1') )
except:
    h = -1
if h > 0:
    ax.set_xlim( matplotlib.dates.epoch2num(data[-1,0]-h*3600), ax.get_xlim()[1] )

# Finish plot
ax.set_ylabel('Temperature F')
for label in ax.get_xticklabels():
    label.set_rotation(60)
plt.tight_layout()

# Save the image to buffer
buf = io.BytesIO()
fig.savefig(buf, format='png')
out = buf.getvalue()
buf.close()
print 'Content-Type: image/png\n'
print out
