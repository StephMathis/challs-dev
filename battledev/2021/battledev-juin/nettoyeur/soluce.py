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
N2 = int(N/2)
debris = input()
cnt1 = collections.Counter()
cnt2 = collections.Counter()
for a in debris[:N2] :
    cnt1[a] += 1
for a in debris[N2:] :
    cnt2[a] += 1

def check(i) :
    A = debris[i:i+N2]
    B = debris[:i] + debris[i+N2:]
    cntA = collections.Counter() 
    cntB = collections.Counter()
    for a in A :
        cntA[a] += 1
    for b in B :
        cntB[b] += 1
    if cntA == cntB :
        return True
    return False

nb = 0
if cnt1 == cnt2 :
    nb += 1
for i in range(1,N2) :
    cnt1[debris[i-1]] -= 1
    cnt2[debris[i-1]] += 1
    cnt1[debris[i-1+N2]] += 1
    cnt2[debris[i-1+N2]] -= 1

    if cnt1 == cnt2 :
        nb += 1
print(nb*2)
