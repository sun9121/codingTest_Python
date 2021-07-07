n = int(input())
n = str(n)
sum_l = 0
sum_r = 0
length = len(n)

for i in range(length):
    if (length/2) > i:
        sum_r += int(n[i])
    else:
        sum_l += int(n[i])

if sum_r == sum_l:
    print("LUCKY")
else:
    print("READY")