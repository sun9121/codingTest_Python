n = int(input())
plan=[]
plan = list(map(str, input().split()))

x, y = 1, 1

for i in range(len(plan)):
    if plan[i] == "L":
        y = y - 1
        if y == 0:
            y = 1
    elif plan[i] == "R":
        y = y + 1
        if y == n+1:
            y = n
    elif plan[i] == "U":
        x = x - 1
        if x == 0:
            x = 1
    elif plan[i] == "D":
        x = x + 1
        if x == n+1:
            x = n

print(x, y, end=' ')