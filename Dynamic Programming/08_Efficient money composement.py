# 화폐의 종류 n, 만들어야하는 가치 m
n, m = map(int, input().split())
# 화폐의 종류를 리스트에 하나하나 가져온다.
mc = []
for i in range(n):
    mc.append(int(input()))
mc.sort() # 작은 값 부터 체크해줘야 하므로 sort를 거쳐준다. 작은 값부터 넣어준다는 문구가 없음

# dp테이블을 만들어준다.
d = [10001]*(m+1) # 밑에서 min을 사용하기 위해서는 m의 최댓값인 10000보다 큰 값을 설정해야한다.
d[0] = 0

for i in range(n):
    for j in range(mc[i], m+1):
        d[j] = min(d[j], (d[j-mc[i]] + 1))

if d[m] == 10001:
    print(-1)
else:
    print(d[m])