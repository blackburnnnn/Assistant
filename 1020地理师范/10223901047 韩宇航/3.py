n=0
for i in range(2,101):
    for x in range(2,i):
        if (i%x)  == 0:
            break
    else:
        print(i,end='\t')
        n+=1
        if n%5==0:
            print()
            
        
