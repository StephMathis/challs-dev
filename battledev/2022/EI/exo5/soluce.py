#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools


N, M, T  = tuple(map(int, input().split()))
steps={}
couts={}
nodes = []
best = {}
for line in sys.stdin :
    i, j, d, c = tuple(map(int, line.rstrip('\r').split()))
    nodes.append(i)
    nodes.append(j)
    steps.setdefault(i,[]).append(j)
    couts[(i,j)] = (d,c)

def getn(i) :
    return steps.get(i,[])

#for n in sorted(list(set(nodes))) :

cout_p = {0:(0,0)}
to_examine = set([0])
while True :
    to_ex = set()
    for i in to_examine :
        voisins = getn(i)
        for v in voisins :
            to_ex.add(v)
            if v in cout_p :
                if cout_p[v][1] > couts[(i,v)][1] + cout_p[i][1] :
                    #print('==> debug :', couts[(i,v)][0] + cout_p[i][0], file=sys.stderr)
                    if M >= (couts[(i,v)][0] + cout_p[i][0]):
                        cout_p[v] = (couts[(i,v)][0] + cout_p[i][0], couts[(i,v)][1] + cout_p[i][1])
            else :
                cout_p[v] = (couts[(i,v)][0] + cout_p[i][0], couts[(i,v)][1] + cout_p[i][1])
        print('==> debug :', cout_p, file=sys.stderr)
    if len(to_ex) == 0 :
        break
    to_examine = set(list(to_ex))
if N in cout_p and cout_p[N][0] <= M :
    print(cout_p[N][1])
else :
    print(-1)


