# key의 1부분과 lock의 0 부분이 맞아야 함

# 인풋을 따로 받아야 할 경우
# import sys
# input = sys.stdin.readline()

# m, n = map(int, input().split())

# key = [[]*m for i in range(m)]
# lock = [[]*n for i in range(n)]

# for _ in range(m):
#     key_line = list(map(int, input().split()))
#     key.append(key_line)

# for _ in range(n):
#     lock_line = list(map(int, input().split()))
#     lock.append(lock_line)

def rotate_matrix_by_90(a): # a = 행렬
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0]*n for _ in range(m)] # 결과 리스트 생성
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock): # new_lock은 길이를 늘이고 키를 더한 자물쇠 행렬 얘기
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
        return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotate_matrix_by_90(key)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j] 

    return False