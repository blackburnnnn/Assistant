s=0
for i in range(1,10):
    for j in range(1,i+1):
        s=i*j
        print('{:.1f}*{:.1f}={:>4.1f}'.format(i,j,s),sep=' ',end=' ')
    print('\n')
