s = input()

count_zero = 0
count_one = 0

for i in range(len(s) - 1):
    if s[i] == '0':
        if s[i+1] == '0':
            continue
        else:
            count_zero +=1
    elif s[i] == '1':
        if s[i+1] == '1':
            continue
        else:
            count_one +=1

count = min(count_zero, count_one)
print(count)