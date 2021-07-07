import math

s = 'xababcdcdababcdcd'

n = int(len(s)/2)
print(n)
count = 1
result = [[] for i in range(n+1)]
length = int(1e9)

for i in range(1, n+1):
    for j in range(1, math.ceil(len(s)/i)+1):
        if s[((j-1)*i):(j*i)] == s[(j*i):((j+1)*i)]:
            count += 1
        else:
            if count == 1:
                result[i].append(s[((j-1)*i):(j*i)])
            elif count >=2:
                result[i].append(str(count) + s[((j-1)*i):(j*i)])
                count = 1
        
    result[i] = "".join(result[i])
    length = min(length, len(result[i]))

# print(result)
print(length)

# 프로그래머스 기준

# import math

# def solution(s):
#     n = int(len(s)/2)
#     count = 1
#     result = [[] for i in range(n+1)]
#     length = int(1e9)
#     for i in range(1, n+1):
#         for j in range(1, math.ceil(len(s)/i)+1):
#             if s[((j-1)*i):(j*i)] == s[(j*i):((j+1)*i)]:
#                 count += 1
#             else:
#                 if count == 1:
#                     result[i].append(s[((j-1)*i):(j*i)])
#                 elif count >=2:
#                     result[i].append(str(count) + s[((j-1)*i):(j*i)])
#                     count = 1

#         result[i] = "".join(result[i])
#         length = min(length, len(result[i]))
        
    
#     answer = length
#     return answer