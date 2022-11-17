for i in range(100000):
    n=int(input())
    a=1
    b=2
    s=0
    if n<=0:
        print('n输入错误')
    else:
        for i in range(1,n+1):
            m=b/a
            s+=m
            a,b=b,a+b
        print('前{:d}项的累加和为{:.2f}'.format(n,s))
