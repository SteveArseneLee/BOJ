import sys
lst = [input().split()]

ascending = True
descending = True

# print(lst)
for i in range(len(lst)):
    if lst[i] > lst[i-1]:
        descending = False
    elif lst[i] < lst[i-1]:
        ascending = False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')