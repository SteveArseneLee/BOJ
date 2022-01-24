def factorial_recursive(x):
    return x * factorial_recursive(x-1) if x > 1 else 1

# T = int(input())
# for _ in range(T):
#     n,m = map(int, input().split())
#     result = factorial(m) // (factorial(n) * factorial(m-n))
#     print(result)

# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial_recursive(m) // (factorial_recursive(n) * factorial_recursive(m - n))
    print(bridge)