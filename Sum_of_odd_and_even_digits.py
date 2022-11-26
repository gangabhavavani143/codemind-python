n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in range(len(x)):
    if i%2==0:
        s+=x[i]
    else:
        c+=x[i]
if (s-c)==0:
    print('YES')
else:
    print('NO')