# heapq의 사용과 인풋최적화를 위한 코드.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 회사의 개수 n, 경로의 개수 m 받아오기 .
n, m = map(int, input().split())
# 경로를 받아오기 위한 리스트 생성.
road = [[] for i in range(n+1)]

# 경로의 개수만큼 a,b로 회사 쌍을 받아서 list에 튜플로 append해준다.
for _ in range(m):
    a, b = map(int, input().split())
    # 거리가 1이니까 그냥 1을 넣어줬다.
    road[a].append((b,1))

# 목표인 회사 x와 소개팅 상대의 장소 k를 받아온다. k를 거친 후 x로 가는 것이 목표.
x, k = map(int, input().split())

# 최단거리 리스트 초기화
distance = [INF] * (n+1)

# 스타트가 1이므로 굳이 받지 않는다.
def dijkstra(start):
    q = []
    # q에 힙푸시로 0,start를 넣는다
    heapq.heappush(q, (0, start))
    # 스타트 지점의 거리를 0으로 해준다
    distance[start] = 0
    while q:
        # 힙에서 거리와 현재 노드 정보를 빼온다.
        dist, now = heapq.heappop(q)
        # distance가 더 작을 때는 의미가 없으니 넘긴다.
        if distance[now] < dist:
            continue
        # road에 저장된 정보를 불러와 하나하나 비교해본다.
        for i in road[now]:
            cost = dist + 1 # 노드간의 거리가 항상 1이기 때문
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 1을 스타트로 다익스트라를 진행해서 k까지의 거리를 저장
dijkstra(1)
kk = distance[k]
# k를 스타트로 dijkstra를 진행, x까지의 거리를 저장 
dijkstra(k)
kx = distance[x]
# 둘을 합친 것을 거리로 한다
dist = kk+kx

# 거리가 INF보다 크거나 같으면 갈 수 없으니 -1표시 아니면 거리 표시
if dist >= INF:
    print('-1')
else: 
    print(dist)