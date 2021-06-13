#! /usr/bin/env python3

#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

N = int(input())

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def get_1_parcours(target) :
    parcours = ''
    for (i,line) in enumerate(lines) :
        parcours += "v"
        parcours_line = ""
        for (j,square) in enumerate(line) :
            parcours_line += ">"
            if square == target :
                parcours_line += "x"
        parcours_line += "<"*(N-1)
        parcours += parcours_line[1:]
    return parcours[1:]
parcours = get_1_parcours("o") + "^"*(N-1) + get_1_parcours("*")
print(parcours)


