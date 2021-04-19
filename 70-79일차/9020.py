# pypy 통과

import math
import sys

p = [] 
for num in range(2, 10001):
    check = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            check = False
            break
    if check:
        p.append(num)
        
def check_num(n):
    one = 0; two = 10001
    for i in range(len(p)):
        v = n - p[i]
        if v in p:
            if p[i] <= v:
                one = p[i]
                two = v
            else:
                break
    return one, two
    
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    n1, n2 = check_num(n)
    print(n1, n2)

