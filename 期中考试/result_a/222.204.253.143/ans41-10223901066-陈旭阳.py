a=int(input('请输入行数：'))
if a%2==1:
    n=1
    while n<=a:
        if n==1:
            print('*'*a)
        if n==a:
            print('*'*a)
        if n!=a and n!=1:
            print(' '*(a//2-1),'*')
        n=n+1
if a%2==0:
    a=a+1
    n=1
    while n<=a:
        if n==1:
            print('*'*a)
        if n==a:
            print('*'*a)
        if n!=a and n!=1:
            print(' '*(a//2-1),'*')
        n=n+1
        

            
