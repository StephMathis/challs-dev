#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

N,M = tuple(map(int,input().split()))
friends = {}
for _ in range(M) :
    a,b = tuple(map(int,input().split()))
    friends.setdefault(a,set()).add(b)
    friends.setdefault(b,set()).add(a)
print(friends.get(1, None),file=sys.stderr)

max_amis_c = 0
k_amis_c = -1
if friends.get(1, None) == None :
    print('-1')
    sys.exit(0) 

for k,amis in friends.items() :
    if k == 1 :
        continue
    if k not in friends[1] :
        continue
    amis_c = friends[1].intersection(amis)
    if len(amis_c) > max_amis_c :
        k_amis_c = k
        print("opt",k,amis_c,file=sys.stderr)
        max_amis_c = len(amis_c)
        continue
    if max_amis_c >0 and (len(amis_c)) == max_amis_c and k_amis_c< k :
        k_amis_c = k

print(k_amis_c)
