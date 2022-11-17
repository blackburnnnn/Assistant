c=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if i!=j and i!=k and j!=k:
               print('%3d'%i,j,k,end='')
               c=c+1
            if c%10==0:
               print('\n')
print('\n')
print('共',c,'个',)
