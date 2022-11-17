#求阶乘之和
n=int(input('n='))
if n<0:
    print('n输入错误!')
    exit(0)
s,t=0,1
if n>0:
    for i in range(1,n+1):
        import math
        t=math.factorial(i)
        s+=t
if n==0:
    s+=t
print('阶乘和为:',s)
