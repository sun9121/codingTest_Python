from collections import deque

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    cities[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for city in cities[now]: # now에서 연결된 도시들을 꺼내온다
        if distance[city] == -1: # 아직 방문하지 않은 도시라면 
            distance[city] = distance[now] + 1 # distance[now] 즉 now의 거리에서 +1 만큼 해준 거리를 입력해준다
            q.append(city) # 그 도시에서 다시 빼울 수 있도록 append 해줌

check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)