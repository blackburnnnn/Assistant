count=0
for i in range(2,100):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print("{:>2d}".format(i),end=' ')
        count=count+1
        if count%5==0:
            print()

        
            
            
            
