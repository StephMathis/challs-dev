#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
# 
import sys
import collections
import math

H, L = map(int,input().split())
sculpt = ['']*H

gauches = [0]*H
droites = [0]*H
i = H
sommet = False
for line in sys.stdin :
    i -= 1
    if not sommet and line.find('X') == -1 :
        H -= 1
        gauches = [0]*H
        droites = [0]*H
        continue
    else : 
        sommet = True

    line = line.rstrip('\n')
    l,r = line.find('X'), line.rfind('X')
    gauches[i] = l
    droites[i] = r
    if l == -1 or (i<H-1 and l > gauches[i+1]) :
        gauches[i] = gauches[i+1]
    if r == -1 or (i<H-1 and r < droites[i+1]) :
        droites[i] = droites[i+1]


def corr_gauche() :
    #print('==> debug gauches :', gauches, file=sys.stderr)
    res = False
    for i in range(2,len(gauches)) :
        if gauches[i-2] == gauches[i] :
            continue
        mid = gauches[i-2] + (gauches[i] - gauches[i-2])/2
        if mid < gauches[i-1] :
            gauches[i-1] = mid
            res = True
    return res

def corr_gauche2() :
    #print('==> debug gauches :', gauches, file=sys.stderr)
    for i in range(2,len(gauches)) :
        if gauches[i-2] == gauches[i] :
            continue
        mid = gauches[i-2] + (gauches[i] - gauches[i-2])/2
        if mid < gauches[i-1] :
            gauches[i-1] = mid
            # on a corrige un point, il faut descendre pour voir jusqu'ou corriger
            j = i-1
            while True and j > 1 :
                midj = gauches[j-2] + (gauches[j] - gauches[j-2])/2
                if midj >= gauches[j-1] :
                    break
                gauches[j-1] = midj
                j -= 1
    return False

def corr_droite() :
    res = False
    for i in range(2,len(droites)) :
        if droites[i-2] == droites[i] :
            continue
        mid = droites[i]+(droites[i-2] - droites[i])/2
        if mid > droites[i-1] :
            droites[i-1] = mid
            res = True
    return res

def corr_droite2() :
    #print('==> debug gauches :', gauches, file=sys.stderr)
    for i in range(2,len(droites)) :
        if droites[i-2] == droites[i] :
            continue
        mid = droites[i-2] + (droites[i] - droites[i-2])/2
        if mid > droites[i-1] :
            droites[i-1] = mid
            # on a corrige un point, il faut descendre pour voir jusqu'ou corriger
            j = i-1
            while True and j > 1 :
                midj = droites[j-2] + (droites[j] - droites[j-2])/2
                if midj <= droites[j-1] :
                    break
                droites[j-1] = midj
                j -= 1
    return False

while corr_gauche2() :
    continue
while corr_droite2() :
    continue

def getl(lines) :
    s = 0
    for i in range(1,len(lines)) :
        s += math.sqrt(1+(lines[i]-lines[i-1])*(lines[i]-lines[i-1]))
    return s
print(math.floor(getl(gauches)+getl(droites)+droites[H-1]-gauches[H-1]))
#print('==> debug :', gauches, file=sys.stderr)
#print('==> debug :', droites, file=sys.stderr)