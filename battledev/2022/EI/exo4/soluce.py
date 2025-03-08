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

tree={}
qtites = {}
fuites = {}
parents={}
enfants={}
feuilles = set()
for line in sys.stdin:
    node = tuple(map(int, line.rstrip('\n').split()))
    if len(node) == 6 :
        n, q, f1, p1, f2, p2 = node
        qtites[n] = q
        fuites[(n,f1)] = p1
        fuites[(n,f2)] = p2
        parents[f2] = n
        parents[f1] = n
        enfants[n] = [f1,f2]
    else :
        n, q = node
        qtites[n] = q
        feuilles.add(n)

def get_sum_qtt(i) :
    if not i in enfants :
        return qtites[i]
    else :
        enf = enfants[i]
        return qtites[i] + get_sum_qtt(enf[0]) + get_sum_qtt(enf[1])

mm=0
for i in range(1,N+1) :
    m = get_sum_qtt(i)*fuites[(parents[i],i)]
    if m > mm :
        mm = m
print(mm)
sys.exit(0)



while True :
    new_f = set()
    s = 0
    for f in feuilles :
        if f == 0 :
            continue
        p = parents[f]
        new_f.add(p)
        qtites[p] += qtites[f]*fuites[(p,f)]
    if len(new_f) == 1 :
        print(qtites[0])
        sys.exit(0)
    feuilles = new_f
