# n,m을 받아준다.
# 미로의 출구가 (n,m)으로 미로의 크기도 그와 같다
# 시작은 1,1
# 탈출하기 위해 움직이는 칸의 개수, 시작이랑 마지막 포함 시작부터 1
n, m = map(int, input().split())

# 미로 정보 입력
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split()))) # 괴물(가지 못하는 부분)은 0, 없는 부분은 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# BFS 방식
# 큐 구조를 사용하기 위해 0,0을 어펜드하고 왼쪽부터 뽑아서 시작하는 구조
from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복한다는 의미
    while queue:
        x, y = queue.popleft()
        # 4방향 탐색해서 1일 때만 움직이면서 2,3... 늘려주기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx<0) or (nx>=n) or (ny<0) or (ny>=m):
                continue
            if maze[nx][ny] == 1:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 2, 3으로 바꾸어주다보면 도착한 지점의 숫자가 곧 거리
                queue.append(nx,ny)

    return maze[n-1][m-1]

print(bfs(0,0))