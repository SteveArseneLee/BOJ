N = int(input())

lst = []

for i in range(N):
    x,y = map(int,input().split())
    lst.append([y,x])
    
lst = sorted(lst)

for i in range(N):
    print(lst[i][1], lst[i][0])