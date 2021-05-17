import sys
import copy
from itertools import combinations

N = int(sys.stdin.readline())
g = []

for _ in range(N):
    g.append(list(sys.stdin.readline().split()))
    
T = []
S = []
X = []
    
for i in range(N):
    for j in range(N):
        if g[i][j] == 'T':
            T.append([i, j])
        elif g[i][j] == 'S':
            S.append([i, j])
        else:
            X.append([i, j])
            
O = list(combinations(X, 3))        

def check(graph):
    for t in T:
        # 위쪽 확인
        up = t[0]
        while up > 0:
            up -= 1
            if graph[up][t[1]] == 'O':
                break
            elif graph[up][t[1]] == 'X' or graph[up][t[1]] == 'T':
                continue
            else:
                return False
        
        # 아래쪽 확인
        down = t[0]
        while down < N-1:
            down += 1
            if graph[down][t[1]] == 'O':
                break
            elif graph[down][t[1]] == 'X' or graph[down][t[1]] == 'T':
                continue
            else:
                return False
            
        # 왼쪽 확인
        left = t[1]
        while left > 0:
            left -= 1
            if graph[t[0]][left] == 'O':
                break
            elif graph[t[0]][left] == 'X' or graph[t[0]][left] == 'T':
                continue
            else:
                return False
            
        # 오른쪽 확인
        right = t[1]
        while right < N-1:
            right += 1
            if graph[t[0]][right] == 'O':
                break
            elif graph[t[0]][right] == 'X' or graph[t[0]][right] == 'T':
                continue
            else:
                return False
    return True
                    
c = False

for o in O:
    G = copy.deepcopy(g)
    G[o[0][0]][o[0][1]] = 'O'
    G[o[1][0]][o[1][1]] = 'O'
    G[o[2][0]][o[2][1]] = 'O'
    if check(G):
        c = True
        break
        
if c:
    print("YES")
else:
    print("NO")