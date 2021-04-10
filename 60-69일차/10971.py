import sys
from itertools import permutations

n = int(sys.stdin.readline()) 
num = [i for i in range(1, n)]
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))
    
permu = list(permutations(num, n-1))
result = int(1e9)

for p in range(len(permu)):
    SUM = 0; c = True
    for i in range(n):
        if i == n-1:
            if g[permu[p][i-1]][0] == 0:
                c = False
                break
            SUM += g[permu[p][i-1]][0]
            continue
        elif i == 0:
            if g[0][permu[p][0]] == 0:
                c = False
                break
            SUM += g[0][permu[p][0]]
            continue
        else: 
            if g[permu[p][i-1]][permu[p][i]] == 0:
                c = False
                break
            SUM += g[permu[p][i-1]][permu[p][i]]
    if c  and result > SUM:
        result = SUM
        
print(result)