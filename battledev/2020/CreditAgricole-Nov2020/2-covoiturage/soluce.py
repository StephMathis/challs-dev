#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

N = int(input().split()[0]) 
# input()
# N,M = tuple(map(int,input().split()))
T = [input().split() for _ in range(N)]
trajets = {}
for nom,dep,arr in T :
    tr = (dep,arr)
    trajets.setdefault(tr,[]).append(nom)
vehicules = []
for tr,pers in trajets.items() :
    p = pers
    while(len(p) > 0) :
        vehicules.append(' '.join(p[:3]))
        p = p[3:]

print(T,file=sys.stderr)

print(len(vehicules))
print('\n'.join(vehicules))
