import sys
N = int(sys.stdin.readline())

for _ in range(N):
    lst = sys.stdin.readline()
    sum = 0
    
    for i in lst:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")