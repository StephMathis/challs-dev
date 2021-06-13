#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
import collections
import itertools

lines = []
for line in sys.stdin :
    lines.append(line.rstrip('\n'))

def check(i) :
    if i > 16 :
        return False
    p = None
    for j in range(len(lines[i])) :
        if lines[i][j] == '.' :
            p=j
    if lines[i+1].count('#') !=9 or lines[i+1][p] != '.': 
        return False
    if lines[i+2].count('#') !=9 or lines[i+2][p] != '.':
        return False
    if lines[i+3].count('#') !=9 or lines[i+3][p] != '.':
        return False
    for h in range(i) :
        if lines[h][p] == '#' :
            return False
    if i + 4 < 20 and lines[i+4][p] == '.' :
        return False
    return p+1


for il, line in enumerate(lines) :
    if line.count('#') == 9 :
        p = check(il)
        if p :
            print("BOOM %d" % (p))
            sys.exit(0)
print('NOPE')

print('==> debug :', lines, file=sys.stderr)

