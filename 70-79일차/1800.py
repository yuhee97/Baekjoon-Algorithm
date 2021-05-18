import sys
import heapq

n, p, k = map(int, sys.stdin.readline().split())
g = [[] for _ in range(1001)]

for _ in range(p): 
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])
    g[b].append([a, c])

def dijkstra(start, limit):
    distance = [INF] * 1001
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        cost, now = heapq.heappop(q)
        if cost > distance[now]:
            continue
        for i in g[now]:
            if i[1] > limit: # 제한값 보다 큰 경우
                if cost + 1 < distance[i[0]]:
                    distance[i[0]] = cost + 1
                    heapq.heappush(q, [cost + 1, i[0]])
            else: # 제한값 보다 작은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, [cost, i[0]])
    if distance[n] > k:  # k 보다 큰 경우(제한값 보다 큰 경우의 수)
        return False
    else:
        return True
      
left, right = 0, 1000001 # 가격을 기준으로 이분탐색
INF = int(1e9)
result = INF

while left <= right: # 이분탐색 이용
    mid = (left + right) // 2
    check = dijkstra(1, mid)
    if check:
        right = mid - 1
        result = mid
    else:
        left = mid + 1
        
if result == INF:
    print(-1) # 연결이 불가능한 경우
else:
    print(result) 