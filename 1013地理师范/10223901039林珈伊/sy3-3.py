a=1
b=1
s=0
n=int(input(''))
if n<=0:
    print('n输入错误')
else:
    for i in range(n):
        a,b=b,a+b
        c=b/a
        s=c+s
    print('前%1.0f项的累加和为%3.2f'%(n,s))
