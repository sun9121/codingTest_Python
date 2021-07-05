n, m = map(int, input().split())

# team = [[]*(m)]

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = []
count = 0
for _ in range(m):
    cal, a, b = map(int, input().split())
    
    if cal == 0:
        union_parent(parent, a, b)

    elif cal == 1:
        count+=1
        if find_parent(parent,a) == find_parent(parent, b):
            result.append('YES')
        else:
            result.append('NO')

for i in range(count):
    print(result[i], end = '\n')

# for i in team:
#     if i[0] == 0:
#         union_parent(parent, i[1], i[2])

#     elif i[0] == 1:
#         if find_parent(parent,a) == find_parent(parent, b):
#             print('YES')
#         else:
#             print('NO')
