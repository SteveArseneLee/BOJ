N = int(input())
# x_lst = []
# y_lst = []
# index = 0

lst = []

for i in range(N):
    [x,y] = map(int,input().split())
    lst.append([x,y])
    
lst = sorted(lst)

for i in range(N):
    print(lst[i][0], lst[i][1])