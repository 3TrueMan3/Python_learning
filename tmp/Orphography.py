word_dict = set()
for i in range(int(input())):
    word_dict.add(str(input()).lower())
ans = set()
for i in range(int(input())):
    for word in input().split(' '):
        if word.lower() not in word_dict:
            ans.add(word)
print('\n'.join(word for word in ans))