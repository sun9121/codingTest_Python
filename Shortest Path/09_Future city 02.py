# heapq의 사용과 인풋최적화를 위한 코드.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 회사의 개수 n, 경로의 개수 m 받아오기 .
n, m = map(int, input().split())
# 경로를 받아오기 위한 리스트 생성.
road = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            road[i][j] = 0

# 경로의 개수만큼 a,b로 회사 쌍을 받아서 list에 튜플로 append해준다.
for _ in range(m):
    a, b = map(int, input().split())
    # 플로이드 워셜을 쓰기위한 방식
    road[a][b] = 1
    road[b][a] = 1

# 목표인 회사 x와 소개팅 상대의 장소 k를 받아온다. k를 거친 후 x로 가는 것이 목표.
x, k = map(int, input().split())

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            road[a][b] = min(road[a][b], road[a][k] + road[k][b])

dist = road[1][k] + road[k][x]

if dist >= INF:
    print('-1')
else: 
    print(dist)