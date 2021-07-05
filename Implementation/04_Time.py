N = int(input())

M_3 = int(60*60)

M = int(15*60 + 45*15)

if N <=2:
    print(M*(N+1))
elif 3<=N<=12: # N이 3일 경우를 고려
    print(M_3+M*N)
elif 13<=N<=22: # N이 3, 13 두 번 지날 경우를 고려
    print(M_3*2+M*N)
elif M == 23: # N이 3, 13, 23 세 번을 지날 경우를 고려
    print(M_3*3+M*21)