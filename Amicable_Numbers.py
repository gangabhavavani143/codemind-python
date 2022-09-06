a=int(input())
b=int(input())
s=0
k=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        k+=j
if s==b and k==a:
    print('Amicable')
else:
    print('Not Amicable')
    
    