import math
n=int(input("n="))
if n<0:
    print("n输入错误!")
    exit(0)
s,t=0,1
if n!=0:
    for i in range(1,n+1):
        t=math.factorial(i)
        s+=t
else:
    s=1
print('阶乘之和为',s)
