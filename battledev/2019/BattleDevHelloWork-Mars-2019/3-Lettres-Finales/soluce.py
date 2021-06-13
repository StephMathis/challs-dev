#! /usr/bin/env python3

#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import itertools

N = int(input())

lines = []
for line in sys.stdin:
    word = line.rstrip('\n')
    lines.append( (len(word), word) )

lines.sort()
word = lines[0][1]
for i in range(len(word), 0, -1) :
    for seq in itertools.combinations(word,i) :
        is_ok = True
        for nb, w in lines[1:] :
            if seq not in itertools.combinations(w,i) :
                is_ok = False
                break
        if is_ok :
            print(''.join(seq))
            sys.exit(0)
print('KO')

