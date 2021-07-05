n = int(input())
list_shop = list(map(int, input().split()))
m = int(input())
list_cstm = list(map(int, input().split()))

for i in range(m):
    count = 0
    for j in range(n):
        if list_shop[j] == list_cstm[i]:
            print('yes', end=' ')
        else:
            count += 1
        
        if count == n:
            print('no', end=' ')