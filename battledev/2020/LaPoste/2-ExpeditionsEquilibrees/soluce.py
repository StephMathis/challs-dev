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
T = [input().split() for _ in range(N)]
T = [ (x[0], int(x[1])) for x in T ]

def mysum(comb) :
    return sum([ x[1] for x in comb])
total = mysum(T)

def myprint(comb) :
    print('==> debug :', comb, file=sys.stderr)
    print(' '.join([x[0] for x in comb ]))
    print(' '.join([ x[0] for x in T if x not in comb]))

mymin = total
myminC = T
for i in range(int(N/2)+1) :
    for comb in itertools.combinations(T,i) :
        a = mysum(comb)
        b = total - a
        d = abs(b - a)
        print('==> debug :', comb, a, b, d, file=sys.stderr)
        if d == 0 :
            myprint(comb)
            sys.exit(0)
        if mymin > d :
            mymin = d
            myminC = comb
myprint(myminC)
print('==> debug :',T, total, file=sys.stderr)

