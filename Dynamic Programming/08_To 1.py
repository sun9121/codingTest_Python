# X값을 받아온다
x = int(input())
# X가 0이상 30000이하이므로 0~30000까지의 30001개의 dp테이블을 만들어준다.
dp = [0]*30001

for i in range(2,x+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[:30])
print(dp[x])