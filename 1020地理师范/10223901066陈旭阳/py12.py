for a in range(1,10):
    b=1
    while b<a:
        print(a,'*',b,"=",a*b,end=' ')
        b=b+1
    while b==a:
        print(a,'*',b,"=",a*b,end='\n')
        b=b+1
        
