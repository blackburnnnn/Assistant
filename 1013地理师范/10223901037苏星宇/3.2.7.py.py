n=0
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            if( i!=j)and(i!=k)and(j!=k)and(i!=0):
             n=n+1
             print(i,j,k,end='\t')
print('共',n,'个')
    
