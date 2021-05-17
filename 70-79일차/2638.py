import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
g = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))
    
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            if g[nx][ny] != 0:
                g[nx][ny] += 1
            else:
                dfs(nx, ny)

def check(g):
    for i in range(n):
        for j in range(m):
            if g[i][j] >= 3:
                g[i][j] = 0
            elif g[i][j] == 0:
                continue
            else:
                g[i][j] = 1
                
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                return False
    return True

time = 0
while True:
    if not check(g):
        visited = [[False] * m for _ in range(n)]
        dfs(0, 0)
        time += 1
    else:
        break
        
print(time)