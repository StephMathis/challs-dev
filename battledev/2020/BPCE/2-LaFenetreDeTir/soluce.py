#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import collections
import itertools

minutes = [0,]*24*60
def myparse(hm) :
    h,m = tuple(map(int,hm.split(':')))
    return 24*h+m
def deparse(hm) :
    return '%02d:%02d' % ((hm//60)%24, hm%60)

input()
for line in sys.stdin :
    line = line.rstrip('\n')
    hms, hme = tuple(map(myparse, line.split('-')))
    for x in range(hms, hme+1) :
        minutes[x] = 'x'
#print(minutes)
dec = minutes.index('x')
#print(dec)
i_m, m = 0, 0
mindec = minutes[dec:] + minutes[0:dec]
for i,v in enumerate(mindec) :
    if v == 'x' :
        continue
    if mindec[i-1] == 'x' :
        mindec[i] = 1
    else :
        mindec[i] = mindec[i-1] +1
    if m < mindec[i] :
        m = mindec[i]
        i_m = i
#print(mindec)

iabs = i_m + dec - m
#print(dec, i_m, m, iabs)
print(deparse(iabs)+'-'+deparse(iabs+m))
