n=int(input())
s=0
a=2
b=1
if n>0:
    for i in range(1,n+1):
        s+=a/b
        t=a
        a=a+b
        b=t
    print('前',n,'项的累加和为',s)
else:
    print('n输入错误')
