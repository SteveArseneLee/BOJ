N = int(input())
lst = []
for _ in range(N):
    x,string = input().split()
    text=''
    for i in string:
        text += int(x) * i
    print(text)