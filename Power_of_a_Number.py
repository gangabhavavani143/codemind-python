import math
x,y,M = map(int,input().split())
p=math.pow(x,y)
r=p%M
print(int(r))
    