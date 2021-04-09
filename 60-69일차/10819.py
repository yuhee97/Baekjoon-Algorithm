# 1번 코드
from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

permu = list(permutations(num, n))
s = 0; m = 0
for i in permu:
    s = 0
    for j in range(n-1):
        s += abs(i[j]-i[j+1])
    if s >= m:
        m = s
print(m)

# 2번 코드
n = int(input())
num = list(map(int, input().split()))
num.sort(); lis = []; SUM = 0

for i in range(n//2):
    if i%2 == 0:
        lis.insert(0, num.pop(0))
        lis.append(num.pop())
    else:
        lis.insert(0, num.pop())
        lis.append(num.pop(0))
        
if n%2 == 1:
    if abs(num[0]-lis[0]) > abs(lis[-1]-num[0]):
        lis.insert(0, num.pop())
    else:
        lis.append(num.pop())

for i in range(n-1):
    SUM += abs(lis[i]-lis[i+1])
        
print(SUM)    