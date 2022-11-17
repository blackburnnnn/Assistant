#Collatz 猜想
N=input('n=')
n=eval(N)
for i in range(1,101):
    if n%2==0:
        n=n/2
        print(n,end=" ")
    else:
         n=3*n+1
         print(n,end=" ")

    i=i+1
    while (n==1):
        print('\n')
        print('猜想正确')
        quit()
    
        
    
       
        
