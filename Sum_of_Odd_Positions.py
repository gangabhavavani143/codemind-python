n=int(input())
s=list(map(int,input().split()))
o=0
for i in range(len(s)):
    if i%2!=0:
        o+=s[i]
print(o)