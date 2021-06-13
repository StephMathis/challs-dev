#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import collections
import itertools

N=int(input())

crypted=input()
target=input()

lcrypted = list(map(ord, crypted))
ltarget = list(map(ord, target))
delta = int((sum(lcrypted) - sum(ltarget))/len(ltarget))

deltas = list(range(26))

def getnbequals(a,b) :
    return sum([ i==j for i,j in zip(a,b) ])

def applydelta(a, delta) :
    return [ ((x+delta)%26)+ord('a') for x in a ]

def getascii(a):
    return ''.join(list(map(chr,a)))

def applydec(a, dec) :
    return a[dec:]+a[:dec]

#print(crypted, target, lcrypted, ltarget, delta)
n_max = 0
best = None
for d in deltas :
    withdelta = applydelta(lcrypted,d)
    for dec in range(len(ltarget)) :
        withdec = applydec(withdelta, dec)
        n = getnbequals(withdec, ltarget)
        if n > n_max :
            n_max = n
            best = withdec
        #print(getascii(withdec), n)
print(getascii(best))
    