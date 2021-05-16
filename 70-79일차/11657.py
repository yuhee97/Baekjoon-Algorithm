import sys

def Bellmanford(start):
    for i in range(n):
        dist[start] = 0
        for j in range(m):
            cur = g[j][0]
            next_node = g[j][1]
            cost = g[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == (n-1):
                    return True
    return False

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
g = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g.append([a, b, c])
    
cycle = Bellmanford(1)

if cycle:
    print(-1)
else:
    for k in range(2, n+1):
        if dist[k] == INF:
            print(-1)
        else:
            print(dist[k])