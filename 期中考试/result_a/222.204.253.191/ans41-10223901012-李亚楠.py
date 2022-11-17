n=int(input('请输入行数:'))
if n%2==0:
    n=n+1
    print('*'*n)
else:
    for i in range(n):
        if i%2 !=0:
            print('*'*n)
       
        
            
