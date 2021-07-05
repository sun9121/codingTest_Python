# 가게의 부품 개수 파악
n = int(input())
# 가게에 있는 물품을 집합 자료형으로 받기
list_shop = set(map(int, input().split()))
# 손님의 구매 개수 파악
m = int(input())
# 손님의 구매 목록 리스트로 받기
list_cstm = list(map(int, input().split()))


# 구매리스트의 물품이 집합 자료 안에 존재하는지 확인
for i in list_cstm:
    if i in list_shop:
        print('yes', end=' ')
    else:
        print('no', end=' ')