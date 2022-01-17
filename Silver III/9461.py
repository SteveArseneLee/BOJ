# 1,1,1,2,2,3,4,5,7,9,12로 되는데...
# 애초에 dp 잡는게 어려웠다...
# dp[n+3] = dp[n] + dp[n+1]

dp = [0] *101
dp[1], dp[2], dp[3] = 1,1,1


for index in range(1,98):
    dp[index+3] = dp[index] +dp[index+1]

a = int(input())
lst = [int(input()) for _ in range(a)]

for i in lst:
    print(dp[i])    

