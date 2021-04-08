import sys

n = int(sys.stdin.readline()) 
s = []
minn = int(1e9)

for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def check(a, b):
    a_S = 0; b_S = 0
    for i in range(n//2):
        for j in range(n//2):
            if i!=j:
                a_S += s[a[i]][a[j]]
                b_S += s[b[i]][b[j]]
    return abs(a_S - b_S)
    
def backtracking(i, A, B):
    global minn
    if len(A) > n//2:
        return
    if len(B) > n//2:
        return
    if i == n:
        v = check(A, B)
        if minn > v:
            minn = v
    backtracking(i+1, A + [i], B)
    backtracking(i+1, A, B + [i])

backtracking(0, [], [])
print(minn)