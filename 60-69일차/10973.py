n = int(input())
now = list(map(int, input().split()))
check = False

for i in range(n-1, 0, -1):
    if now[i-1] < now[i]:
        continue
    else:
        check = True
        for j in range(i, n):
            if now[i-1] > now[j]:
                idx = j
        v = now[idx]
        now[idx] = now[i-1]
        now[i-1] = v
        result = now[0:i] + now[::-1][0:n-i]
        break
        
if not check:
    print(-1)
else:
    print(*result, end = " ")
