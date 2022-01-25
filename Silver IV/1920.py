# # 1. 방법
# N, A = int(input()), {i: 1 for i in map(int, input().split())}
# # i: 1 for i in map(int, input().split())}의 의미
# # 입력받은 수를 다 쪼개서 int로 바꾼 후 있는 수들은 1로 매칭, 없는 수들은 참조를 못하고 error
# M = input()
# for i in list(map(int, input().split())):
#     # print(A[i]) => Error 뜸
#     print(A.get(i,0))
#     # print(A.get(i, "false"))
#     # get이란 메소드는 dictionary에서 아직 등록이 안된 애들은 0으로 출력


# ---------------------------------------

# 2. dictionary 쓰는 방법
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')


# ---------------------------------------


# # 3. 쉬운 방법
# for i in list(map(int, input().split())):
#     print(1 if i in A else 0)