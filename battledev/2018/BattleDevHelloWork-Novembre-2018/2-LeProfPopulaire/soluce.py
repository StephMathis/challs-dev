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
T = [list(map(int,input().split())) for _ in range(N)]

def is_ok(comb) :
    comb = list(comb)
    comb.sort()
    for i in range(1,len(comb)) :
        if comb[i] - comb[i-1] <= 60 :
            return False
    return True

for n in range(N,1,-1) :
    for etudiants in itertools.combinations(T, n) :
        print(n, etudiants, file=sys.stderr)
        for comb in itertools.product(*etudiants) :
            if is_ok(comb) :
                print(n)
                sys.exit(0)
            print(comb, is_ok(comb), file=sys.stderr)

print(T,file=sys.stderr)
