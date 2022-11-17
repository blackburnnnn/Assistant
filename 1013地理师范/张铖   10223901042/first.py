for i in range(5):
    n=int(input())
    a=1
    b=1
    s=0
    if n<=0:
        print('n输出错误')
    else:
        for i in range(n):
            c=a
            a=a+b
            b=c
            s+=a/b
        print('前{:d}项的累加和为{:4.2f}'.format(n,s))
