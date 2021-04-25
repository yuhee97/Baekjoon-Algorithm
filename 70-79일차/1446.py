import heapq
import sys
    
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        print(q)
        dist, now  = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in g[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                print(1)
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance[d]

n, d = map(int, input().split())
g = [[] for _ in range(10001)]
distance = [i for i in range(10001)]
    
for i in range(n):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    
print(dijkstra(0, distance))