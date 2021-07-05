# import time
# start_time = time.time()

n, m = map(int, input().split())

card_list=[]
max_list = []
for i in range(n):
    card_list.append(list(map(int, input().split())))
    max_list.append(min(card_list[i]))

print(max(max_list))

# end_time = time.time()

# print("time :", end_time-start_time)