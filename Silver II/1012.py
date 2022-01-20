import sys
T = int(input())
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().rstrip().split())
    spot = [
        input().split()
        for _ in range(K)
    ]
    print(spot)