import sys 

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
    
def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
node = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append([c, a, b])
    
edges.sort()
parent = [i for i in range(node+1)]
result = 0

for i in edges:
    cost, a, b = i
    if find_parent(a) != find_parent(b):
        result += cost
        union_find(a, b)

print(result)
