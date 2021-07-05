location = input()
count = 0
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

x = location[0]
y = int(location[1])
x = int(ord(x)) - int(ord('a')) + 1

for i in range(8):
    mx = x + dx[i]
    my = y + dy[i]

    if (1<=mx<=8) and (1<=my<=8): # 나는 이렇게 했지만 최대한 따로따로 논리연산자를 나누는게 좋다!
        count += 1
    else:
        continue

print(count)
