lst = [input() for _ in range(int(input()))]
alphabets = [0 for i in range(26)]

for word in lst:
    a = 0
    while word:
        now = word[-1]
        alphabets[ord(now) - ord('A')] += pow(10,a)
        # print(now,alphabets[ord(now) - ord('A')])
        a+=1
        word = word[:-1]

# print(alphabets)
alphabets.sort(reverse=True)
# print(alphabets)

ans = 0
for i in range(9,0,-1):
    # print(i, alphabets[9-i])
    ans += i * alphabets[9-i]
    # print(ans)
print(ans)