import sys

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
minn = int(1e9)

def check(a, b):
    a_S = 0; b_S = 0
    for i in a:
        for j in a:
            if i==j:
                continue
            a_S += s[i][j]
    for i in b:
        for j in b:
            if i==j:
                continue
            b_S += s[i][j]
    return abs(a_S - b_S)
    
def backtracking(i, A, B):
    global minn
    if i == n:
        if len(A) == 0:
            return
        if len(B) == 0:
            return
        v = check(A, B)
        if minn > v:
            minn = v
        return
    backtracking(i+1, A + [i], B)
    backtracking(i+1, A, B + [i])
    return minn

print(backtracking(0, [], []))