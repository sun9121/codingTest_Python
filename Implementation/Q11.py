n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 # 1이 사과가 있음을 뜻함

rotate = []
l = int(input()) # 뱀의 방향전환 횟수
for _ in range(l):
    x, c = input().split()
    rotate.append((int(x),c))

head = 0
# 동남서북 0123
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 처음 위치
    board[x][y] = 2 # 뱀이 있으면 2로 표시
    direction = 0 # 뱀의 방향
    t = 0 # 시간
    index = 0 # 회전 정보
    q = [(x,y)] # 뱀이 차지하는 위치

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1<=nx and nx<=n and 1<=ny and ny<=n and board[nx][ny]!=2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                board[px][py] = 0
            
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))
        
        else:
            t += 1
            break

        x, y = nx, ny
        t += 1
        if index < l and t == rotate[index][0]:
            direction = turn(direction, rotate[index][1])
            index += 1
    return t

print(simulate())