k=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
        k=k+1
        if k%5==0:
            print('\n')
        
    
