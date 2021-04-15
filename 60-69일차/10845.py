import sys

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(q) > 0:
            print(q.pop(0))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)