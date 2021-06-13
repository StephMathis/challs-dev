#! /usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

input()
users = []
for line in sys.stdin:
	users.append(list(map(int,line.rstrip('\n').split())))

scores = [(sum(user),user,i+1) for i,user in enumerate(users)]
scores.sort()
#scores.reverse()
while True :
    old = scores[:]
    scores=[scores[0]]
    for s,u,i in old[1:] :
        #print(s,u,i,scores[-1])
        a = u[0] < scores[-1][1][0]
        b = u[1] < scores[-1][1][1]
        c = u[2] < scores[-1][1][2]
        if a+b+c>=2 :
            scores.append(scores[-1])
            scores[-2] = (s,u,i)
        else :
            scores.append((s,u,i))

    if old == scores :
        break
print(' '.join(['%s' % s[2] for s in scores]))
