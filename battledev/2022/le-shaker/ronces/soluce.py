#! /usr/bin/env python3

#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
#sys.setrecursionlimit(100000000)

input()
MAX=9999

cle=None
i = 0
lines = []
grille = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    grille.append([MAX]*len(line))
    o = line.find('O')
    if o>=0 :
        cle = (i,o)
    i+=1
W = len(lines[0])
H = len(lines)


def getneighboors(pos) :
    res = [(pos[0]-1,pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0],pos[1]+1) ]
    res = [ x for x in res if x[0]>=0 and x[0]<H and x[1]>=0 and x[1]<W ]
    return res

def isX(c) :
    return lines[c[0]][c[1]] == 'X' 

def getG(grille, pos) :
    return grille[pos[0]][pos[1]]

def setG(grille, pos, v) :
    grille[pos[0]][pos[1]] = v

def debug(grille) : 
    for line in grille :
        t = ''
        for c in line :
            if c == MAX:
                t+='.. '
            else : 
                t+= "%02d " % c
        print(t, file=sys.stderr)

def rect(grille, pos) :
    c_pos = getG(grille, pos)
    for c in getneighboors(pos) :
        c_c = getG(grille, c)
        if c_c == MAX :
            continue
        if c_pos < c_c :
            if isX(c) :
                if c_pos < c_c - 1:
                    setG(grille, c, c_pos+1)
                    rect(grille, c)
            else : 
                setG(grille, c, c_pos) 
                rect(grille, c)

def fillcell(grille, pos) :
    mymin = min([ getG(grille, c) for c in getneighboors(pos)])
    if mymin == MAX :
        if isX(pos) :
            setG(grille, pos, 1)
        else :
            setG(grille, pos, 0)
    else :
        setG(grille, pos, mymin)
        if isX(pos) :
            setG(grille, pos, mymin+1)
    rect(grille, pos)
    return 

def getmin() :
    mygrille = []
    for l in lines :
        mygrille.append([MAX]*len(lines[0]))
    for i in range(len(lines)) :
        for j in range(len(lines[0])) :
            fillcell(mygrille, (i,j))
    A = getG(mygrille, cle)
    print("A", A, file=sys.stderr)
    debug(mygrille)
    
    mygrille = []
    for l in lines :
        mygrille.append([MAX]*len(lines[0]))
    for i in range(len(lines),0,-1) :
        for j in range(len(lines[0]),0,-1) :
            fillcell(mygrille, (i-1,j-1))
    B = getG(mygrille, cle)
    print("B", B,  file=sys.stderr)
    debug(mygrille)
    return A+B

print("%d" % (getmin()))
