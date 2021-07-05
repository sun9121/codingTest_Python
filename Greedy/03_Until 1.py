N, K = map(int, input().split())
count = 0

# while True: 
#     if N == 1:
#         break
#     if N % K != 0:
#         N = N - 1
#         count += 1
#     else:
#         N = N/K
#         count += 1

while True:
    count += N%K
    N = N - count
    N = int(N/K)
    count += 1
    if N < K:
        break
count -= (N-1)
print(count)