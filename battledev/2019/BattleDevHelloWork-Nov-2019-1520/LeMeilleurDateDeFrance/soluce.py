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


print(T,file=sys.stderr)

