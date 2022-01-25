# # 내가 짠 코드
# T = int(input())
# lst = [
#     int(input())
#     for _ in range(T)
# ]

# lst.sort()

# for i in lst:
#     print(i)

# ------------------------
# # 1. 선택정렬 알고리즘
# n = int(input())
# array = list()

# for _ in range(n):
#     array.append(int(input()))
    
# for i in range(n):
#     min_index = i # 가장 작은 원소의 인덱스
#     for j in range(i+1, n):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

# for i in array:
#     print(i)

