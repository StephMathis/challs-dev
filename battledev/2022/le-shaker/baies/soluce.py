#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

from re import M
import sys
import collections
import itertools


a,b,c = tuple(map(int, input().split()))
sac = [a,b,c]
print('==> debug :', 'sac', sac, file=sys.stderr)
N = int(input()) 
# input()
# N,M = map(int,input().split())
recettes = [tuple(map(int, input().split())) for _ in range(N)]

def sac_minus_recette(sac, recette, n) :
    s = sac[:]
    for i in range(3) :
        s[i] -= n*recette[i]
    return s

def getmax(sac, recette) :
    mymin = float('inf')
    for i in range(3) :
        if recette[i] != 0 and mymin>sac[i]/recette[i] :
            mymin = sac[i]//recette[i]
    return mymin

def getpower(sac, recettes, comb) :
    s = sac[:]
    p = 0
    for i,c in enumerate(comb) :
        for j in range(3) :
            s[j] -= c*recettes[i][j]
            if s[j] < 0 :
                return -1
        p += c*recettes[i][3]
    return p

if False :
    combi = [list(range(0, getmax(sac, r)+1)) for r in recettes]
    N = 1
    for c in combi :
        N *= len(combi)
    print('==> debug :', 'N', N, file=sys.stderr)
    mymax = 0
    mymaxcomb = None


    for comb in itertools.product(*combi) :
        m = getpower(sac, recettes, comb)
        if m > mymax :
            mymax = m 
            mymaxcomb = comb
        #print('==> debug :', 'comb', comb, m, file=sys.stderr)


def getmymax(sac, recettes, max_recettes) :
    mymax = -1
    mymaxpos = []
    if len(max_recettes) == 0 :
        return (0, mymaxpos)
    for i in range(max_recettes[0]+1) :
        newsac = sac_minus_recette(sac, recettes[0], i)
        if any([s<0 for s in newsac]) :
            break
        mm, mmpos = getmymax(newsac, recettes[1:], max_recettes[1:])
        if mm < 0 :
            break
        m = i*recettes[0][3] + mm
        if m > mymax :
            mymax = m
            mymaxpos = [i] + mmpos
    return (mymax, mymaxpos)

max_recettes = [getmax(sac, r) for r in recettes]
print(getmymax(sac, recettes, max_recettes))


#print('==> debug :', recette, getmax(sac, recette), file=sys.stderr)
#perr
#print('==> debug :', recettes,file=sys.stderr)

