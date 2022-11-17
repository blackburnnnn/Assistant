a=int(input('请输入一个数：'))
if a%2==0:
    a=a+1
else:
    for i in range(a) :
        d=str(a)
        b=d[0]
        c=d[-1]
        if i==b:
            x=0
            while x<=a:
                print('*',end='')
                x=x+1
        elif i==c:
            print('*'*a)
        else:
            print('*')
