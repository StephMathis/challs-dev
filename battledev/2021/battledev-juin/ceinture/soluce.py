#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

N, A, C = map(int,input().split())
asters = list(map(int,input().split()))
print('==> debug :', N, A, C, file=sys.stderr)


#res=[ sum(asters[i:i+A]) for i in range(A+C) ]
sA = sum(asters[:A])
res = [sA]
for i in range(1,A+C) :
    sA += asters[i+A-1]-asters[i-1]
    res.append(sA)
m = res[0]
sA = res[-1]
for i in range(A+C, len(asters)) :
    if m < res[-C-A] :
        m = res[-C-A]
    sA -= asters[i-1]
    sA += asters[i+A-1] if i+A <= len(asters) else 0
    res.append(sA+m)
    #print('==> debug :', i, sA, m, res, file=sys.stderr)
#print('==> debug :', res, file=sys.stderr)
print(sum(asters)-max(res[-C-A:]))
