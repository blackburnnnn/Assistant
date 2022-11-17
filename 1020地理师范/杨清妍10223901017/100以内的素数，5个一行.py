count=0
for i in range(2,101):
     for j in range(2,i):
        if i%j==0:
             break
     else:
        count+=1
        print('{:>2}'.format(i),end='\t')
        if count%5==0:
            print( )
                
