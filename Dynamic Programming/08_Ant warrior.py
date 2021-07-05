# 창고의 갯수 받아오기
N = int(input())
# 창고의 정보 받아오기
store = list(map(int, input().split()))
# dp 테이블 만들기(3<=N<=100)
d = [0]*N

d[0] = store[0]
d[1] = max(store[0], store[1])

for i in range(2,N):
    a = d[i-1]
    b = store[i] + d[i-2]
    d[i] = max(a,b)

print(d[N-1])