m=0
for i in range(2,101):
    a=False
    for j in range(2,i):
        if i%j==0:
            break
    else:
            m+=1
            print(i,end=" ")
            if m%5==0:
                print( )
            
