m=int(input())
n=int(input())
s=0
c=0
for i in range(1,m):
    if m%i==0:
        s+=i
for i in range(1,n):
    if n%i==0:
        c+=i
if s==n or c==m:
    print("Amicable")
else:
    print("Not Amicable")