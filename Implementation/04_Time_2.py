# Use 'For'
# 완전탐색을 하고도 메모리가 충분하겠다 싶으면 이런식으로 짜버리는 것도 나쁘지 않다.

h = int(input())
count=0
# 문자열로 묶는 방법
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count+=1

# 나머지를 계산해서 확인하는 방법
# 조금 더 전통적인 사고방식이라 구상하기 쉬운대신 조건이 많아서 조금 더 걸릴지도?? 이 부분은 잘 모르겠음
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if (i%10==3) or (j%10==3) or (k%10==3) or (i//10==3) or (j//10==3) or (k//10==3):
                count+=1
print(count)