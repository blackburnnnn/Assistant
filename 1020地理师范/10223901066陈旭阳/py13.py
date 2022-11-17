n=0
for a in range(1,101):
    k=0
    for b in range(1,a+1):
        if a%b==0:
            k=k+1
    if k==2:
        print(a,end=' ')
        n=n+1
        if n==5:
            print()
            n=0
        
            
        
        
