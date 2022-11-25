n=int(input())
x=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(x)):
    if x[i]%2!=0:
        c.append(x[i])
    else:
        d.append(x[i])
print(*(c+d))