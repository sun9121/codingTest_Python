n = int(input())
coins = list(map(int, input().split()))
coins.sort()

sum = 1

for i in coins:
    print(sum)
    # 만들 수 없는 금액을 찾았을 때 종료
    if sum < i:
        break
    sum += i

print(sum)