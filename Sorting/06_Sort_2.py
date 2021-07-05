# 성적이 낮은 순서로 학생 출력하기
n = int(input())

def setting(data):
    return data[1]

test = []

test = [input().split() for _ in range(n)]

for i in range(n):
    test[i][1] = int(test[i][1])

test_sort = sorted(test, key=setting)

for i in range(n):
    print(test_sort[i][0], end=' ')