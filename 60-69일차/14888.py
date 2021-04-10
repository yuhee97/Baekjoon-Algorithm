from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
now_op = []

for i in range(len(op)):
    if op[i] >= 1:
        now_op += [i] * op[i]
        
permu = set(list(permutations(now_op, n-1)))
 
minn = int(1e9)
maxx = -int(1e9)

for p in permu:
    v = num[0]
    for i in range(n-1):
        if p[i] == 0: # 덧셈
            v += num[i+1]
        elif p[i] == 1: # 뺄셈
            v -= num[i+1]
        elif p[i] == 2: # 곱셈
            v *= num[i+1]
        else: # 나눗셈
            if v < 0:
                v = -(abs(v)//num[i+1])
            else:
                v //= num[i+1]
    if minn >= v:
        minn = v
    if maxx <= v:
        maxx = v

print(maxx)
print(minn)