n=int(input())
a=2
b=1
c=0
f=0
i=0
s=0
if n>0:
    for i in range(n) :
        f=a/b
        s=s+f
        c=b
        b=a
        a=a+c
    print('前%d项的累加和为%.2f'%(n,s))
if n<=0:
    print('n输入错误')
    
