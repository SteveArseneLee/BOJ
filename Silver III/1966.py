# test_case = int(input())

# for _ in range(test_case):
#     n, m = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     key = list(range(len(imp)))
#     key[m] = 'target'
    
#     order = 0
    
#     while True:
#         # 첫번째 if - imp의 첫번째 값이 최댓값인가?
#         if imp[0] == max(imp):
#             order += 1
            
#             # 두번째 if - key의 첫번째 값이 'target'인가?
#             if key[0] == 'target':
#                 print(order)
#                 break
#             else:
#                 imp.pop(0)
#                 key.pop(0)
#         else:
#             imp.append(imp.pop(0))
#             key.append(key.pop(0))

# -----------------------------------------------------
test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))