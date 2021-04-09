import math

n = int(input())
now = [i for i in range(1, n+1)]
print(*now, end = " ")
entire = math.factorial(n)-1

while entire != 0:
    idx = 0
    for i in range(n-1, 0, -1):
        if now[i-1] > now[i]:
            continue
        else:
            check = True
            for j in range(i, n):
                if now[i-1] < now[j]:
                    idx = j
            v = now[idx]
            now[idx] = now[i-1]
            now[i-1] = v
            result = now[0:i] + now[::-1][0:n-i]
            print()
            print(*result, end = " ")
            break
    now = result
    entire -= 1