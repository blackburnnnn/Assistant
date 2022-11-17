n=int(input('请输入n的值'))
if n<=0:
    print('n输入错误')
if n>0:
    s=0
    i=1
    b=1
    c=1
    d=b+c
    a=d/c
    while i<=n:
        s=s+a
        b=c
        c=d
        i=i+1
    print(s)
        
