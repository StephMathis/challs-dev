#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

H, L = map(int,input().split())
sculpt = ['']*H
upper_left = None
lower_left = None
upper_right = None
lower_right = None
i_lower_left, i_lower_right = None, None
i = H
for line in sys.stdin :
    line = line.rstrip('\n')
    i -= 1
    sculpt[i] = line
    left = line.find('X')
    right = line.rfind('X')
    if upper_left == None :
        upper_left = lower_left = left
        upper_right = lower_right = right
        i_lower_left, i_lower_right = i, i
    if lower_right < right and right != -1 :
        lower_right = right
        i_lower_right = i

drap_gauche = [(i_lower_left, lower_left),(H-1, upper_left)]
i_drap = i_lower_left
for i in range(i_lower_left+1, H-1) :
    left = sculpt[i].find('X')
    if left == -1 :
        continue
    ref = drap_gauche[i_drap][1] + (drap_gauche[i_drap+1][1]-drap_gauche[i_drap][1])*1.0*(i-drap_gauche[i_drap][0])/(drap_gauche[i_drap+1][0]-drap_gauche[i_drap][0])
    if ref < left :
        continue
    else : 
        drap_gauche = drap_gauche[:i_drap+1]
        drap_gauche.append((i, left))
        drap_gauche += drap_gauche[i_drap+1:]
        i_drap += 1

drap_droit = [(i_lower_right, lower_right),(H-1, upper_right)]
i_drap = i_lower_right
for i in range(i_lower_right+1, H-1) :
    rigth = sculpt[i].rfind('X')
    if rigth == -1 :
        continue
    ref = drap_droit[i_drap][1] + (drap_droit[i_drap+1][1]-drap_droit[i_drap][1])*1.0*(i-drap_droit[i_drap][0])/(drap_droit[i_drap+1][0]-drap_droit[i_drap][0])
    if ref > rigth :
        continue
    else : 
        drap_droit = drap_droit[:i_drap+1]
        drap_droit.append((i, rigth))
        drap_droit += drap_droit[i_drap+1:]
        i_drap += 1


