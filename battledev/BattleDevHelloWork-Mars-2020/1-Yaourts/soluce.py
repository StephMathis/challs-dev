#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys


import collections
c = collections.Counter()
sys.stdin
for line in sys.stdin :
    c[line.rstrip('\n')] += 1
for (a,b) in c.most_common(2) :
    print(a, end=' ')
print()

