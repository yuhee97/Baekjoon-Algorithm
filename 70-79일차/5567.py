from collections import deque

n = int(input())
m = int(input())
g = [[] for _ in range(501)]
visited = [0] * 501

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs():
    q = deque()
    visited[1] = 1
    c = 0
    for i in g[1]:
        visited[i] = 1
        q.append(i)
        c += 1
    while q:
        x = q.popleft()
        for j in g[x]:
            if visited[j] == 0:
                visited[j] = 1
                c += 1
    return c

print(bfs())