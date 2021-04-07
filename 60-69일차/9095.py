# recursion
def recursion(n):
    global answer
    if n == 0:
        answer += 1
    if n > 0:
        recursion(n-1)
        recursion(n-2)
        recursion(n-3)

T = int(input())

for i in range(T):
    answer = 0
    recursion(int(input()))
    print(answer)

# dp
def dynamic():
    global dp
    dp[1] = 1; dp[2] = 2; dp[3] = 4
    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())
dp = [0] * 12
dynamic()

for i in range(T):
    print(dp[int(input())])

