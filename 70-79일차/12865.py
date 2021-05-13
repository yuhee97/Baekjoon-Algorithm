n, k = map(int, input().split())
dp = [[0] * (k+1) for i in range(n+1)]
W = [0]
V = [0]

for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, n+1):
    for j in range(1, k+1):
        if W[i] > j:
            dp[i][j] = dp[i-1][j]        
        else:
            dp[i][j] = max(dp[i-1][j-W[i]]+V[i], dp[i-1][j])

print(max(dp[n]))