n, m = map(int, input().split())

edges = []
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cost, a, b = map(int, input().split())

    edges.append((cost, a, b))

edges.sorts()
cost_sum = 0
last = 0 # 신장트리를 두 부분으로 나누기 위해서 가장 큰 부분을 삭제해준다. 그럼 최소 조건에 맞게끔 나뉘겠지.

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost_sum += cost
        last = cost

print(cost_sum - last)