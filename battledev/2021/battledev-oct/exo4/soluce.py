#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

input()
sculpt = []
most_left = None
most_right = None
drap_gauche = []
drap_droite = []
for line in sys.stdin :
    left = line.find('X')
    right = line.rfind('X')
    if len(drap_gauche) == 0 :
        drap_gauche.append(left)
        drap_droite.append(right)
        continue
    if len(drap_gauche) == 1 :
        if left>=0 and left < drap_gauche[0]:
            drap_gauche.append(left)
        else :
            drap_gauche.append(drap_gauche[0])
        if right>=0 and right < drap_droite[0]:
            drap_droite.append(drap_droite[0])
        else :
            drap_droite.append(right)
        continue
    if left == -1 or left > drap_gauche[-1] :
        drap_gauche.append(drap_gauche[-1])
    else :
        if drap_gauche[-1] - left > drap_gauche[-2] - drap_gauche[-1] :
            drap_gauche[-1] = left + 0.5*(drap_gauche[-2]-left)
            drap_gauche.append(left)
        else :
            drap_gauche.append(left)
    if right < drap_droite[-1] :
        drap_droite.append(drap_droite[-1])
    else :
        if right - drap_droite[-1]  > drap_droite[-2] - drap_droite[-1] :
            drap_droite[-1] = right + 0.5*(drap_droite[-2]-right)
            drap_droite.append(right)
        else :
            drap_droite.append(right)




    

    
    drap_gauche.append(line.find('X'))
    drap_droite.append(line.rfind('X'))

def rect(drap_gauche) :
    res = [drap_gauche[0]]
    if drap_gauche[1] == -1 :
        res.append(res[-1])
    else :
        if drap_gauche[1] > res[-1] :
            drap_gauche[1]


    for i in range(1,len(drap_gauche)) :
        if drap_gauche[i] == -1 :
            res.append(res[-1])
            continue
        if 






