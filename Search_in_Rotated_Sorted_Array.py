n=int(input())
x=list(map(int,input().split()))
a=int(input())
for i in range(len(x)):
    if a in x:
        if x[i]==a:
            print(i)
            break
    else:
        print(-1)
        break