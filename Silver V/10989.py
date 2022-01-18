# N = int(input())
# # lst = [int(input()) for _ in range(N)]
# lst = [0] *10001



# lst.sort()
# for i in lst:
#     print(i)

# sys.stdin.readlin()을 사용하면 속도가 빨라지고 메모리가 작아짐
import sys

N = int(input())
lst = [0] *10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    lst[input_num] += 1 # 각 칸에 몇개씩 있는지 추가
    # print(lst[input_num])

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)