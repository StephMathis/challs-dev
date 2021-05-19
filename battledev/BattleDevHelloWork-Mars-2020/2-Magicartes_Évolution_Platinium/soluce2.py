#! /usr/bin/env python3
# 
import sys
import collections
import itertools

if False :
    #n = "3" 
    #sachaline = "eau sol poison glace sol plante poison eau glace vol"
    #mycardsline = "plante plante sol sol feu plante plante plante sol feu"
    n = "10"
    sachaline = "sol glace eau plante sol eau eau plante poison vol"
    mycardsline = "sol plante sol feu plante feu plante sol plante plante"
else :
    n = input()
    sachaline = input()
    mycardsline = input()

sacha = sachaline.rstrip('\n').split(' ')
mycards = mycardsline.rstrip('\n').split(' ')

weakers = {}
weakers['eau'] = ['feu']
weakers['feu'] = ['plante', 'glace']
weakers['plante'] = ['eau', 'poisson', 'vol']
weakers['sol'] = ['eau', 'plante']

strongers = {}
for (elem,items) in weakers.items() :
    for item in items :
        strongers.setdefault(item, []).append(elem)

def i_win(mygame, sacha) :
    if len(sacha) == 0 and len(mygame) > 0 :
        return True
    if len(mygame) == 0 :
        return False
    if mygame[0] in weakers and sacha[0] in weakers[mygame[0]] :
        return i_win(mygame, sacha[1:])
    if mygame[0] in strongers and sacha[0] in strongers[mygame[0]] :
        return i_win(mygame[1:], sacha)
    return i_win(mygame[1:], sacha[1:])


for game in itertools.permutations(mycards, len(mycards)) :
    game = list(game)
    if i_win(game, sacha) :
        print(' '.join(game))
        sys.exit(0)
print("-1")