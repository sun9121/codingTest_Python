s = input() # 문자열 받기
# 그냥 문자열 두 문자열 중 왼쪽에 0이 있으면 + 나머지는 다 *를 하면 된다.
sum = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or sum <= 1:
        sum = sum + num
    else:
        sum = sum * num

print(sum)