#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

N = int(input()) 
# input()
# N,M = tuple(map(int,input().split()))
T = [input() for _ in range(N)]

def getmin(hm) :
    h,m = map(int, hm.split(':'))
    return h*60 + m - 8*60

day=[False,]*((20-8)*60)
for reu in T :
    start,end = reu.split('-')
    for a in range(getmin(start), getmin(end)) :
        day[a] = True
s=0
cnt = 0
for i in day :
    if i :
        if cnt >= 60 :
            s+=cnt
        cnt = 0
        continue
    cnt += 1
if cnt >= 60 :
    s += cnt
print('==> debug :',T,file=sys.stderr)
#print('==> debug :', day, file=sys.stderr)
print(s)
