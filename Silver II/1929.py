# M,N = map(int, input().split())
# lst = []
# def prime(x):
#     # 1은 무조건 안됨
#     if x == 1:
#         return False
#     # 2부터 (x-1)까지 모든 수 확인
#     for a in range(2,x):
#         # x가 해당 수로 나누어 떨어지면
#         if x % a == 0:
#             return False # 소수 아님
#     return True
    

# for i in range(M, N+1):
#     if prime(i): print(i)

# 에라토스테네스의 체 활용
# 에라토스테네스의 체란 일정 범위내 수열에서 배수들을 제거해 소수만 남기는 방법
# [2 3 4 5 6 7 8 9 10]에서 2의 배수 제거
# [2 3 5 7 9]에서 3의 배수 제거
# [2 3 5 7]

def prime(x):
    if x == 1: return False
    else:
        for n in range(2, int(x**0.5)+1):
            if x % n == 0:
                return False
        return True

M,N = map(int, input().split())

for i in range(M, N+1):
    if prime(i): print(i)