def floyd(d):
    for k in range(1, n+1):
        for i in range(n+2):
            for j in range(n+2):
                if i == j:
                    continue
                if d[i][k] < 1001 and 1000 - d[k][j] > -1:
                    d[i][j] = 0
    if d[0][n+1] == 0:
        return True
    else:
        return False
    
t = int(input())
for _ in range(t):
    n = int(input())
    g = []; graph = [[0] * (n+2) for _ in range(n+2)]
    for _ in range(n+2):
        g.append(list(map(int, input().split())))
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue
            graph[i][j] = abs(g[i][0]-g[j][0])+abs(g[i][1]-g[j][1])  
            
    if abs(g[0][0]-g[n+1][0])+abs(g[0][1]-g[n+1][1]) <= 1000:
        print('happy')
    elif n != 0:
        if floyd(graph):
            print('happy')
        else:
            print('sad')
    else:
        print('sad')