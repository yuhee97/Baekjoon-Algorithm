import sys

def function(D, distance, graph):
    for i in range(0, D+1):
        if i != 0:
            distance[i] = min(distance[i], distance[i-1]+1)
        for a, b, c in graph:
            if a == i and distance[i]+c < distance[b]:
                distance[b] = distance[i]+c
    return distance[D]

n, d = map(int, sys.stdin.readline().split())
distance = [i for i in range(10001)]
g = []
    
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    g.append([a, b, c])
    
print(function(d, distance, g))
