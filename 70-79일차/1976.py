import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
g = [[] for _ in range(n+1)]

def dijkstra(start, end):
    q = []
    heapq.heappush(q, [0, start])
    dist = [INF] * (n+1)
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in g[now]:
            cost = i[1] + d
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
                
    if dist[end] == INF:
        return False
    else:
        return True
    
            
for i in range(1, n+1):
    N = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        if N[j-1] == 1:
            g[i].append([j, 1])
            
route = list(map(int, sys.stdin.readline().split()))
result = True

for i in range(m-1):
    check = dijkstra(route[i], route[i+1])
    if check:
        continue
    else:
        result = False
        break
        
if result:
    print('YES')
else:
    print('NO')