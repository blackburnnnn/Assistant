n=int(input('n='))
while n%2==0:
    n=n/2
    print(int(n),'',end="")
    if n==1:
        quit()
    while n%2==1:
        n=3*n+1
        print(int(n),'',end="")
while n%2==1:
    n=3*n+1
    print(int(n),'',end="")
    while n%2==0:
        n=n/2
        print(int(n),'',end="")
        if n==1:
            quit()
       
      
