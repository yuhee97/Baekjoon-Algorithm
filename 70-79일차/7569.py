import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
graph = []

dz = [1, -1, 0, 0, 0, 0] #  앞뒤
dx = [0, 0, 0, -1, 0, 1] # 위아래
dy = [0, 0, 1, 0, -1, 0] # 왼쪽/오른쪽

for _ in range(h):
    g = []
    for _ in range(n):
        g.append(list(map(int, sys.stdin.readline().split())))
    graph.append(g)

cn = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                cn.append([i, j, k])
            
def bfs():
    q = deque()
    for c in cn:
        i, j, k = c
        visited[i][j][k] = 1
        q.append([i, j, k])
    while q:
        z, x, y = q.popleft()
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append([nz, nx, ny])

bfs()                        
check = True
maxx = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                check = False
            if visited[i][j][k] > maxx:
                maxx = visited[i][j][k]
                
if check:
    print(maxx-1)
else:
    print(-1)