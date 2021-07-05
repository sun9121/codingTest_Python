n = int(input())
numbers =[]

# numbers = [int(input() for _ in range(n))] # 아래와 같지만 컴프리헨션으로 구현

for _ in range(n):
    numbers.append(int(input()))

sor = sorted(numbers, reverse=True)

for i in range(n):
    print(sor[i], end=' ')