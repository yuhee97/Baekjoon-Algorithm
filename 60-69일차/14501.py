# dp
import sys

n = int(sys.stdin.readline()) 
t = [0]; p =[0]
dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a); p.append(b)
    
for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[i])
    if i+t[i]-1 > n:
        continue
    dp[i+t[i]-1] = max(dp[i-1] + p[i], dp[i+t[i]-1])
    
print(max(dp))

# recursion
import sys

n = int(sys.stdin.readline()) 
t = [0]; p =[0]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a); p.append(b)
    
store = []

def recursion(result, i):
    if i == n+1:
        store.append(result)
        return
    if i > n+1:
        return
    recursion(result+p[i], i+t[i])
    recursion(result, i+1)
    
recursion(0, 1)
print(max(store))