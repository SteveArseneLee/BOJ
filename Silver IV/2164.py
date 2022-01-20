# import sys

# N = int(sys.stdin.readline())
# stack = list(range(1,N+1))

# while (len(stack)>1):
#     stack.pop(0)
#     stack.append(stack.pop(0))

# print(stack[0])

import sys
from collections import deque

n = int(input())
stack = deque(range(1,n+1))
while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack.pop())