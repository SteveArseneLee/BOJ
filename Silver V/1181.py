lst = []

for i in range(int(input())):
    lst.append(input())
    
set_list = list(set(lst)) # 중복제거

sorted_list = []

for j in set_list:
    sorted_list.append((len(j),j))
    
sorted_list.sort()

for len_word,i in sorted_list:
    print(i)