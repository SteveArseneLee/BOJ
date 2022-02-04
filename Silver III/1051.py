N,M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]

max_size = 1

for i in range(N):
    for j in range(M):
        for k in range(max_size,50):
            if N<=i+k or M<=j+k:
                break
            if len(set([lst[i][j],lst[i+k][j],lst[i][j+k],lst[i+k][j+k]])) == 1:
                max_size = max(max_size,k+1)

print(max_size**2)
