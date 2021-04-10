n = int(input())
g = dict()

for _ in range(n):
    a, b, c = input().split()
    g[a] = [b, c]
    
def preorder(parent):
    print(parent, end = "")
    if g[parent][0] != '.':
        preorder(g[parent][0])
    if g[parent][1] != '.':
        preorder(g[parent][1])

def inorder(parent):
    if g[parent][0] != '.':
        inorder(g[parent][0])
    print(parent, end = "")
    if g[parent][1] != '.':
        inorder(g[parent][1])

def postorder(parent):
    if g[parent][0] != '.':
        postorder(g[parent][0])
    if g[parent][1] != '.':
        postorder(g[parent][1])
    print(parent, end = "")
    
preorder('A')
print()
inorder('A')
print()
postorder('A')