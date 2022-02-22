# 최대공약수
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

# 최소공배수
def lcm(a, b):
    return int(a*b/gcd(a,b))

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a,b))

# --------------------
# math module 사용 시
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))