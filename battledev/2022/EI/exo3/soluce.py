#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

first = input()
second = input()
N = int(input()) 

for xx in itertools.combinations([1,2,3,4,5,6,7,8,9],5) :
    for x in itertools.permutations(xx,5) :
        s1 = x[0]*10000+x[1]*1000+x[2]*100+x[3]*10+x[4]
        s2 = ""
        for s in second :
            s2 += "%s" % x[first.find(s)]
        if int(s2)+s1 == N :
            print(s1)
            sys.exit(0)
