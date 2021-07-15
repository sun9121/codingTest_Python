# n,m을 받아준다.
n, m = map(int, input().split())

# 얼음 틀 정보 입력
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split()))) # 구멍이 뚫려있으면 0, 아니면 1

# 방문기록을 생성하고 더이상 방문할 수 없으면 하나
def dfs(x,y):
    # (n,m)범위를 벗어나지 않도록
    if (x>=n) or (x<=-1) or (y<=-1) or (y>=m):
        return False
    
    if ice[x][y] == 0:
        # 방문처리
        ice[x][y] = 1
        # 연결된 부분 모두 호출
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)