n=int(input('n='))
for i in range(1,100):
    if n%2==0:
        n/=2
        print('%d'%(n),end=' ')
    else:
        n=3*n+1
        print('%d'%(n),end=' ')
    while (n==1):
        quit()
    
    
