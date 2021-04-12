import sys

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    
v, e = map(int, sys.stdin.readline().split())
g = []; result = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    g.append([c, a, b])

g.sort()
parent = [i for i in range(v+1)]

for i in g:
    cost, a, b = i
    if find_parent(a) != find_parent(b):
        result += cost
        union_parent(a, b)
    
print(result)