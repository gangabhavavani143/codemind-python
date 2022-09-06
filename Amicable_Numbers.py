n=int(input())
m=int(input())
s=0
c=0
for i in range(1,n):
    if n%i==0:
       # print(i)
        s+=i
for l in range(1,m):
    if m%l==0:
        #print(l)
        c+=l
if s==m and c==n:
    print("Amicable")
else:
    print("Not Amicable")