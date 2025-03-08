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
# N,M = map(int,input().split())
T = [input() for _ in range(N)]

N, M = tuple(map(int, input().split()))
line =""
N, M = tuple(map(int, line.rstrip('\r').split()))


#perr
print('==> debug :', T,file=sys.stderr)


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
