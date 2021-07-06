n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 공의 무게가 달라야만 조합이 의미가 있다.
b = len(balls)
count = 0

for i in range(b):
    for j in range(i + 1, b):
        if balls[i] != balls[j]:
            count += 1
        else:
            continue

print(count)

# 천 미만이라 이중for문이 상관 없을 것 같기는 하지만... m을 따로 제시한 것을 보면 이러한 방식의 풀이를 원했던 것 같지는 않다. 아닌가?