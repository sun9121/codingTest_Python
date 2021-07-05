# 떡의 개수 N, 손님이 요청한 길이 M을 int로 받기
N, M = map(int, input().split())
# 모든 떡의 개별 길이를 rc에 list로 받기
rc = list(map(int, input().split()))

# 이진탐색을 위한 값을 설정해준다.
start = 0
end = max(rc)
result = 0
while start <= end:
    sum = 0
    mid = (start + end) // 2

    for tteok in rc:
        if tteok > mid:
            sum += tteok - mid
    
    if sum < M:
        end = mid -1
          
    else:
        result = mid
        start = mid + 1
         
print(result)
