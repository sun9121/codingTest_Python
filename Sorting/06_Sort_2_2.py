# 삽입 정렬 직접 구현을 통한 문제 풀이
n = int(input())

test = []

for i in range(n):
    s, t = input().split()
    test.append((s,int(t)))

for i in range(1,n):
    for j in range(i, 0, -1):
        if test[j][1] < test[j-1][1]:
            test[j], test[j-1] = test[j-1], test[j]
        else:
            break

for i in range(n):
    print(test[i][0], end=' ')

# array = []
# for i in range(n):
#     array.append(test[i][1])

