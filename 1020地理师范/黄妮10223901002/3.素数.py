count=0
for n in range(2,100):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=' ')
        count+=1
        if count%5==0:
            print()
    
