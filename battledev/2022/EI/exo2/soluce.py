#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools


C,M = tuple(map(int, input().split()))
chauffages = sorted(list(map(int, input().split())))
homes = sorted(list(map(int, input().split())))

s = 0
chauff = chauffages[:]
for h in homes :
    for c in chauffages :
        if c >= h :
            s += c
            continue
print(s)




