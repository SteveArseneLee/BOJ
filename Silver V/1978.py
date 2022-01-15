count = 0

# 소수 판별
def prime(x):
    # 1은 무조건 안됨
    if x == 1:
        return False
    # 2부터 (x-1)까지 모든 수 확인
    for a in range(2,x):
        # x가 해당 수로 나누어 떨어지면
        if x % a == 0:
            return False # 소수 아님
    return True

n = int(input())
numbers = map(int, input().split())

for i in numbers:
    if prime(i):
        count += 1

print(count)