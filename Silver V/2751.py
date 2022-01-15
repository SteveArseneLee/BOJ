N = int(input())
lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort()
for i in lst:
    print(i)

# num = sorted(set(lst))
# for j in range(N):
#     print(num[j])