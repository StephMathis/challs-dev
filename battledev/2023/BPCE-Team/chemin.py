import heapq
import sys


input()

cle=None
i = 0
lines = []
grille = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    o = line.find('O')
    if o>=0 :
        cle = (i,o)
    i+=1
W = len(lines[0])
H = len(lines)

def get_neighbors(coord) :
    res = [(coord[0]-1,coord[1]), (coord[0]+1, coord[1]), (coord[0], coord[1]-1), (coord[0],coord[1]+1) ]
    res = [ x for x in res if x[0]>=0 and x[0]<H and x[1]>=0 and x[1]<W ]
    return res

def get_weight(coord1, coord2) :
    if lines[coord2[0]][coord2[1]] == 'X' :
        return 1
    return 0

def dijkstra(f_get_neighbors, f_get_weight, source, target) :
    ##assert all(weight[u][v]>=0 for u in range(n) for v in graph[u])
    prec = {}
    black = {} #[False]*n
    dist = {} #[float('inf')]*n
    dist[source] = 0
    heap = [(0,source)]
    while heap :
        dist_node, node = heapq.heappop(heap) # le sommet le plus proche
        if not black.get(node, False) :
            black[node] = True
            if node == target :
                break
            for neighbor in f_get_neighbors(node) :
                dist_neighbor = dist_node + f_get_weight(node,neighbor)
                if dist_neighbor < dist.get(neighbor, float('inf')) :
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] =  node
                    heapq.heappush(heap, (dist_neighbor, neighbor))
    return dist[target], prec

print(dijkstra(get_neighbors,get_weight, (0,0), cle)[0])
print(dijkstra(get_neighbors,get_weight, cle, (W-1, H-1))[0])
print('==> debug :', file=sys.stderr, flush=True)