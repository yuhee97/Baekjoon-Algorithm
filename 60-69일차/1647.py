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
        
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
result = 0; g =[]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g.append([c, a, b])
    
g.sort()
c = 0

for i in g:
    cost, a, b = i
    if find_parent(a) != find_parent(b):
        result += cost
        union_parent(a, b)
        if c < cost:
            c = cost

print(result-c)