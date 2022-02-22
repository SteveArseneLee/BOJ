r = 0

for i in list(map(int, input().split())):
    r += i**2
print(r%10)

# 더 짧은 코드
# print(sum([n**2 for n in map(int, input().split())]) % 10)