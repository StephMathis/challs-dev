#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import collections

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

sys.stderr.write(n)
sys.stderr.write('\n')
sys.stderr.write(sachaline)
sys.stderr.write('\n')
sys.stderr.write(mycardsline)
sys.stderr.write('\n')
sys.stderr.write('\n')
sys.stderr.write('\n')

sacha = sachaline.rstrip('\n').split(' ')
mycards = collections.Counter()
for card in mycardsline.rstrip('\n').split(' ') :
    mycards[card] += 1
#print(sacha, mycards)



weakers = {}
weakers['eau'] = ['feu']
weakers['feu'] = ['plante', 'glace']
weakers['plante'] = ['eau', 'poisson', 'vol']
weakers['sol'] = ['eau', 'plante']

strongers = {}
for (elem,items) in weakers.items() :
    for item in items :
        strongers.setdefault(item, []).append(elem)

mydeck = []
i_sacha = 0
while i_sacha < len(sacha) :
    c = sacha[i_sacha]
    found = False
    if not c in strongers :
        # rien n'est plus fort, il faut trouver une carte qui ne soit pas plus faible
        if c not in weakers :
            # n'importe quelle carte convient
            # j'en prends une
            mycard = mycards.most_common(1)[0][0]
            mydeck.append(mycard)
            mycards[mycard] -= 1
            found = True
        else :
            # on cherche une carte dans mycards qui ne soit pas dans les weakers[c]
            for t in mycards :
                if t not in weakers[c] :
                    mydeck.append(t)
                    mycards[t] -= 1
                    found = True
    else :
        # on recherche un carte plus forte 
        for s in strongers[c] :
            if s in mycards :
                mydeck.append(s)
                mycards[s] -= 1
                found = True
                break
        if not found :
            # on cherche une carte égale
            if c in mycards :
                mydeck.append(c)
                mycards[c] -= 1
                found = True
    if not found :
        print("-1")
        sys.exit(0)
    else :
        i_sacha += 1
        while i_sacha < len(sacha) :
            if not sacha[i_sacha] in weakers.get(mydeck[-1], []) : 
                break
            i_sacha += 1

    sys.stderr.write("%d\n" % i_sacha)
    sys.stderr.write(' '.join(mydeck))
    sys.stderr.write('\n')
    sys.stderr.write('\n')
for t,c in mycards.items() :
    mydeck +=  [t]*c
print(' '.join(mydeck))

                    
