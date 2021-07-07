s = input()
alpha = []
num = 0

for i in s:
    if ord(i) >= 65:
        alpha.append(i)
    elif ord(i) < 60:
        num += int(i)

alpha.sort()
alpha = "".join(alpha)
print(alpha + str(num))