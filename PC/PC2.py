s=input()
n=1221
for i in range(n):
    s+=input()
i=0
CS=[]
for i in range(len(s)):
    CS.append(int(s.count(s[i])))
    i+=1
i=0
for i in range(len(s)):
    if CS[i]==1:
        print(s[i])
