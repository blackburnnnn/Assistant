for i in range(1, 10):
    for j in range(1,i+1):
        print('{:2.1f}*{:2.1f}={:2.1f}\t'.format(i,j,i*j),end='')
    print()
