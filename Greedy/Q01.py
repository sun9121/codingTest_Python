n = int(input()) # 모험가의 명수 # 모든 모험가를 내보내야 하는 건 아님
fear = list(map(int, input().split())) # 모험가의 공포도 리스트
fear.sort() # 정렬 시키기

ppl = 0
group = 0

for i in fear:
    ppl += 1
    if ppl == i:
        group += 1
        ppl = 0

print(group)