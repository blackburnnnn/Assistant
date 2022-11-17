n=int(input('n='))
if n<=0:
    print('n输入错误！')
    exit(0)
else:
    a,b,s,i=1,2,0,1
    while i<=n:
        s=s+b/a
        a,b=b,a+b
        i=i+1
    print(f'{s:.2f}')
