b=0
for i in range(2,101):
    a=0
    for n in range(1,101):
        if i%n==0:
            a+=1
    if a==2:
        print(i,end=" ")
        b=b+1
        if b%5==0:
            print()
            
                
                    
    
