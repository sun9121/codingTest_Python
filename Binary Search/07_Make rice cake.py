# 떡의 개수 N, 손님이 요청한 길이 M을 int로 받기
N, M = map(int, input().split())
# 모든 떡의 개별 길이를 rc에 list로 받기
rc = list(map(int, input().split()))
# cutter의 길이
C = max(rc) - 1
mid = 0

# 이진탐색
def binary_search(target, array, start, end):
    global N
    global mid
    if start > end:
        print(mid)
        return mid + 1
    mid = (start + end) // 2
    if target == array[mid]:
        print(mid)
        return mid
    elif array[mid] < target:
        return binary_search(target, array, mid+1, end)
    else:
        return binary_search(target, array, start, mid-1)

# 커터의 값을 가진 리스트를 설정해주기
# cutter = [C-i for i in range(C)]

# 손님이 가져가는 떡의 길이를 저장하기 위한 리스트
customer = []

for i in range(C):
    # rest를 매번 0으로 초기화
    rest = 0

    for j in range(N):
        # 떡의 길이가 cutter보다 길 때 잘린 길이만큼 다 더하여 customer에 더해준다.
        if rc[j] >= (C-i):
            rest += (rc[j] - (C-i))
        else:
            continue

    # 길이의 합 만큼 costomer에 append 해줌
    customer.append(rest)

print(customer)

result = binary_search(M, customer, 0, C-1)
print(C-result)