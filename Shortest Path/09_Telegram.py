import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

# dijkstra를 사용하기 위한 리스트 초기화
board = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    board[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in board[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

# 전보 전달 가능 도시 수를 카운트 하기 위한 함수
count = 0
distance_max = [] # 난 리스트를 따로 만들어줘서 append이후에 max를 일괄적으로 해줬는데 한번씩 max를 해줘서 비교하는게 더 빠르려나??
for i in distance:
    if i < INF:
        count += 1
        distance_max.append(i)

print(count-1, max(distance_max), sep=' ')