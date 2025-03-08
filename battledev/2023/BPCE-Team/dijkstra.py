import sys
import heapq


lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


w, h = map(int, lines[0].split())
grid = lines[1:]

pta = ptb = None
for r in range(h):
    for c in range(w):
        if grid[r][c] == 'A':
            pta = (r, c)
        if grid[r][c] == 'B':
            ptb = (r, c)

def dijkstra(grid, pt1, pt2):
    tovisit = [(0, pt1)]
    dst = {pt1: 0}
    while tovisit:
        d, node = heapq.heappop(tovisit)
        if node == pt2: return d
        r, c = node
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neigh = (r + dr, c + dc)
            if 0 <= r + dr < h and 0 <= c + dc < w and neigh not in dst:
                newdist = dst[node] + int(grid[r+dr][c+dc] == '#')
                dst[neigh] = newdist
                heapq.heappush(tovisit, (newdist, neigh))


print(dijkstra(grid, pta, ptb))
