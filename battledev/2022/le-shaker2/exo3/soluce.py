#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

autruche = sorted([ list(map(int, input().split())) for _ in range(3)])
N = int(input()) 
ciel = sorted([ list(map(int, input().split())) for _ in range(N)])


def mydiff(l1, l2) :
    return [ y-x for x,y in zip(l1,l2) ]

def is_same(autruche, etoiles) :
    delta = mydiff(autruche[0], etoiles[0])
    for x in [1,2] :
        d = mydiff(autruche[x], etoiles[x])
        if not delta == d :
            return False
    return True 

for trois in itertools.combinations(ciel,3):
    if is_same(autruche, trois) :
        for x,y in trois :
            print(x, y)
        sys.exit(0)
print("NOT FOUND")

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def path(coord):
    print(coord)
