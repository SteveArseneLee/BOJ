# # # Union-Find 알고리즘
# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         p = find(parent[x])
#         parent[x] = p
#         return parent[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
    
#     parent[y] = x

# parent = []

# for i in range(0,5):
#     parent.append(i)
    
# union(1,4)
# union(2,4)

# for i in range(1, len(parent)):
#     print(find(i), end=' ')


# ----------------------------

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()
    
    f = int(input())
    
    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])