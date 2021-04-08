# permutation
from itertools import permutations

n = int(input()) 
sign_can = [str(i) for i in range(0, 10)]
sign = list(input().split())

permu = permutations(sign_can, n+1)
result = []

for p in permu:
    check = True
    for i in range(len(p)-1):
        if sign[i] == ">":
            if not int(p[i]) > int(p[i+1]):
                check = False
                break
        else:
            if not int(p[i]) < int(p[i+1]):
                check = False
                break
    if check:
        result.append(''.join(p))

print(result[-1])
print(result[0])

# backtracking
def check(one, two, op):
    if op == "<":
        if not one < two:
            return False
    else:
        if not one > two:
            return False
    return True
            
result = []
def backtracking(i, now):
    if i > n+1:
        return
    if len(now) == n+1:
        result.append(now)
        return
    for j in range(10):
        if c[j]:
            continue
        if i == 0 or check(int(now[-1]), j, sign[i-1]):
            c[j] = True
            backtracking(i+1, now+str(j))
            c[j] = False

c = [False] * 10
n = int(input()) 
sign = list(input().split())
backtracking(0, '')
result.sort()
print(result[-1])
print(result[0])