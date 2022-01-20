N, M = map(int, input().split())
lst = list(map(int,input().split()))

result = 0
length = len(lst)
for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1, length):
            sum_value = lst[i] + lst[j] + lst[k]
            if sum_value <= M:
                result = max(result, sum_value)

print(result)