n, m = map(int, input().split()) # 판의 크기 x축N y축M
x, y, d = map(int, input().split()) #캐릭터의 위치 x,y 바라보는 방향 d
#북동남서가 0123으로 회전 순서는 반시계 방향이므로 03210321... 의 식이다
# 3번째 입력부터 맵에 대한 정보를 알려준다. 0은 육지 1은 바다

board = []
for _ in range(m):
    board.append(list(map(int, input().split())))
count = 0 # 돌아간 횟수 설정
move = [[0,-1], [1,0], [0,1], [-1,0]] # d에 맞는 전진 이동 방향

move_count = 1 # 방문 칸 수. 처음 칸을 포함해 1로 시작
board[x][y] = 2 # 가본 칸을 2로 만든다.

while True:
    if count == 4: # 회전을 4번 했다면 뒤로 가야하므로 -를 해준다
        dx = x-move[d][0]
        dy = x-move[d][1]
        if board[dx][dy] == 1: # 뒤로 갔는데 바다면 종료
            break
        else: # 뒤가 바다가 아니라면 일단 이동하고 다음으로 넘어가서 회전함
            x = dx
            y = dy
            count = 0
    if d == 0: # 회전하는 부분 0이면 3으로 간다.
        d = 3
        count += 1
    else: # 0이 아닌 경우는 -1씩 해주면 시계방향으로의 회전임
        d = d - 1
        count += 1
    
    # 회전 이후에 이동 지점을 예측하는 부분
    dx = x + move[d][0]
    dy = y + move[d][1]

    if board[dx][dy] == 0: # 예측 지점이 1:바다, 2:이미이동한지점이 아닌 경우 이동
        x = dx
        y = dy
        board[dx][dy] = 2
        count = 0
        move_count += 1 # 0으로 이동했으므로 방문칸 +1
    else:
        continue # 0이 없다면 포문 처음으로 돌아가서 회전

print(move_count) # 방문 칸 출력