

SmokePing Targets:  

Filter:



 - Charts              
 - Local               
 - Internet            
    
 - PlusnetISP          
 - Google              
 - BBC                 

Internet

ERROR: opening '/var/lib/smokeping/Internet/Plusnet.rrd': No such file or directory
'DEF:median1=/var/lib/smokeping/Internet/Plusnet.rrd:median:AVERAGE'
'DEF:loss1=/var/lib/smokeping/Internet/Plusnet.rrd:loss:AVERAGE'
'CDEF:ploss1=loss1,20,/,100,*'
'CDEF:dm1=median1,0,100000,LIMIT'
'DEF:pin1p1=/var/lib/smokeping/Internet/Plusnet.rrd:ping1:AVERAGE'
'CDEF:p1p1=pin1p1,UN,0,pin1p1,IF'
'DEF:pin1p2=/var/lib/smokeping/Internet/Plusnet.rrd:ping2:AVERAGE'
'CDEF:p1p2=pin1p2,UN,0,pin1p2,IF'
'DEF:pin1p3=/var/lib/smokeping/Internet/Plusnet.rrd:ping3:AVERAGE'
'CDEF:p1p3=pin1p3,UN,0,pin1p3,IF'
'DEF:pin1p4=/var/lib/smokeping/Internet/Plusnet.rrd:ping4:AVERAGE'
'CDEF:p1p4=pin1p4,UN,0,pin1p4,IF'
'DEF:pin1p5=/var/lib/smokeping/Internet/Plusnet.rrd:ping5:AVERAGE'
'CDEF:p1p5=pin1p5,UN,0,pin1p5,IF'
'DEF:pin1p6=/var/lib/smokeping/Internet/Plusnet.rrd:ping6:AVERAGE'
'CDEF:p1p6=pin1p6,UN,0,pin1p6,IF'
'DEF:pin1p7=/var/lib/smokeping/Internet/Plusnet.rrd:ping7:AVERAGE'
'CDEF:p1p7=pin1p7,UN,0,pin1p7,IF'
'DEF:pin1p8=/var/lib/smokeping/Internet/Plusnet.rrd:ping8:AVERAGE'
'CDEF:p1p8=pin1p8,UN,0,pin1p8,IF'
'DEF:pin1p9=/var/lib/smokeping/Internet/Plusnet.rrd:ping9:AVERAGE'
'CDEF:p1p9=pin1p9,UN,0,pin1p9,IF'
'DEF:pin1p10=/var/lib/smokeping/Internet/Plusnet.rrd:ping10:AVERAGE'
'CDEF:p1p10=pin1p10,UN,0,pin1p10,IF'
'DEF:pin1p11=/var/lib/smokeping/Internet/Plusnet.rrd:ping11:AVERAGE'
'CDEF:p1p11=pin1p11,UN,0,pin1p11,IF'
'DEF:pin1p12=/var/lib/smokeping/Internet/Plusnet.rrd:ping12:AVERAGE'
'CDEF:p1p12=pin1p12,UN,0,pin1p12,IF'
'DEF:pin1p13=/var/lib/smokeping/Internet/Plusnet.rrd:ping13:AVERAGE'
'CDEF:p1p13=pin1p13,UN,0,pin1p13,IF'
'DEF:pin1p14=/var/lib/smokeping/Internet/Plusnet.rrd:ping14:AVERAGE'
'CDEF:p1p14=pin1p14,UN,0,pin1p14,IF'
'DEF:pin1p15=/var/lib/smokeping/Internet/Plusnet.rrd:ping15:AVERAGE'
'CDEF:p1p15=pin1p15,UN,0,pin1p15,IF'
'DEF:pin1p16=/var/lib/smokeping/Internet/Plusnet.rrd:ping16:AVERAGE'
'CDEF:p1p16=pin1p16,UN,0,pin1p16,IF'
'DEF:pin1p17=/var/lib/smokeping/Internet/Plusnet.rrd:ping17:AVERAGE'
'CDEF:p1p17=pin1p17,UN,0,pin1p17,IF'
'DEF:pin1p18=/var/lib/smokeping/Internet/Plusnet.rrd:ping18:AVERAGE'
'CDEF:p1p18=pin1p18,UN,0,pin1p18,IF'
'DEF:pin1p19=/var/lib/smokeping/Internet/Plusnet.rrd:ping19:AVERAGE'
'CDEF:p1p19=pin1p19,UN,0,pin1p19,IF'
'DEF:pin1p20=/var/lib/smokeping/Internet/Plusnet.rrd:ping20:AVERAGE'
'CDEF:p1p20=pin1p20,UN,0,pin1p20,IF'
'CDEF:pings1=20,p1p1,UN,p1p2,UN,+,p1p3,UN,+,p1p4,UN,+,p1p5,UN,+,p1p6,UN,+,p1p7,UN,+,p1p8,UN,+,p1p9,UN,+,p1p10,UN,+,p1p11,UN,+,p1p12,UN,+,p1p13,UN,+,p1p14,UN,+,p1p15,UN,+,p1p16,UN,+,p1p17,UN,+,p1p18,UN,+,p1p19,UN,+,p1p20,UN,+,-'
'CDEF:m1=p1p1,p1p2,+,p1p3,+,p1p4,+,p1p5,+,p1p6,+,p1p7,+,p1p8,+,p1p9,+,p1p10,+,p1p11,+,p1p12,+,p1p13,+,p1p14,+,p1p15,+,p1p16,+,p1p17,+,p1p18,+,p1p19,+,p1p20,+,pings1,/'
'CDEF:sdev1=p1p1,m1,-,DUP,*,p1p2,m1,-,DUP,*,+,p1p3,m1,-,DUP,*,+,p1p4,m1,-,DUP,*,+,p1p5,m1,-,DUP,*,+,p1p6,m1,-,DUP,*,+,p1p7,m1,-,DUP,*,+,p1p8,m1,-,DUP,*,+,p1p9,m1,-,DUP,*,+,p1p10,m1,-,DUP,*,+,p1p11,m1,-,DUP,*,+,p1p12,m1,-,DUP,*,+,p1p13,m1,-,DUP,*,+,p1p14,m1,-,DUP,*,+,p1p15,m1,-,DUP,*,+,p1p16,m1,-,DUP,*,+,p1p17,m1,-,DUP,*,+,p1p18,m1,-,DUP,*,+,p1p19,m1,-,DUP,*,+,p1p20,m1,-,DUP,*,+,pings1,/,SQRT'
'CDEF:dmlow1=dm1,sdev1,2,/,-'
'CDEF:s2d1=sdev1'
'AREA:dmlow1'
'AREA:s2d1#00458630::STACK'
'LINE1:dm1#004586:med RTT'
'VDEF:avmed1=median1,AVERAGE'
'VDEF:avsd1=sdev1,AVERAGE'
'CDEF:msr1=median1,POP,avmed1,avsd1,/'
'VDEF:avmsr1=msr1,AVERAGE'
'GPRINT:avmed1:%5.1lf %ss av md '
'GPRINT:ploss1:AVERAGE:%5.1lf %% av ls'
'GPRINT:avsd1:%5.1lf %ss av sd'
'GPRINT:avmsr1:%5.1lf %s am/as\l'


Maintained by 
Stu

Running on SmokePing-2.6.8 by Tobi Oetiker and Niko Tyni




