from itertools import combinations

while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    n = n[1:]
    n.sort()
    combi = list(combinations(n, 6))
    for c in combi:
        print(*c, end = " ")
        print()
    print()