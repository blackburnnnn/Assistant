for i in range(1,10):
    for j in range(1,i+1):
        print('{:.1f}*{:.1f}={:.1f}'.format(i,j,i*j),end=' ')
    print()
