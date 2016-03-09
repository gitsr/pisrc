# resolutions
# 1 day @ 1 minute
# 4 weeks @ 5 minute
# 2 years @ 1 hour

rrdtool create elec.rrd --start 0 --step=60 \
DS:joules:COUNTER:6000:U:U \
RRA:AVERAGE:0.5:1:60       \
RRA:AVERAGE:0.5:5:8064     \
RRA:AVERAGE:0.5:60:17520
