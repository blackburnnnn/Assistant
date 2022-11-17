n=int(input())
s=0
t=1
a=1
b=2
for i in range(1,n+1):
    t=a/b
    s+=t
    b=a+b
    a=b-a
if n<=0:
    print('n输入错误')
    exit(0)
else:
    print('前',n,'项的累加和为',s)
