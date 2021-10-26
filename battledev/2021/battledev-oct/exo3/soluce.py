#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

N, H = map(int,input().split())
paysage = []
for line in sys.stdin :
    l = []
    for x in line : 
        if x == '-' :
            l.append(0)
        else :
            l.append(1)
    paysage.append(l)

def getnb(x,y) :
    s = 0
    s+= sum(paysage[x][y:y+3])
    s+= sum(paysage[x+1][y:y+3])
    s+= sum(paysage[x+2][y:y+3])
    return s

res = []
for x in range(N-3+1) :
    for y in range(H-3+1) :
        res.append((getnb(x,y),x, y))
res.sort()
#print('==> debug :', paysage, file=sys.stderr)

#print('==> debug :', res, file=sys.stderr)

print(res[-1][1]-1,res[-1][2]-1)

