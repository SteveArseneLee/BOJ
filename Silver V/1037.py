# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

N = int(input())
lst = []

for i in range(N):
    lst.append(input())

set_lst = []
for i in lst:
    set_lst.append((len(i),i))

result = sorted(set_lst)
