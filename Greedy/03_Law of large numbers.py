# 92p 큰 수의 법칙

n, m, k = map(int, input().split())
list = [int(i) for i in input().split()]

list.sort()

largest_num_1, largest_num_2 = list[-1], list[-2]

count = 0
sum = 0

for _ in range(m):
    if count == 0:
        sum += largest_num_1
        count += 1
    elif count % k != 0:
        sum += largest_num_1
        count += 1
    else:
        sum += largest_num_2
        count += 1

print(sum)