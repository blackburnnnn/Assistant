for i in range(1,10):
    for j in range(1,i+1):
        result=i*j
        print('{:0.1f}*{:0.1f}={:0.1f}'.format(i,j,result),end='\t')
    print()
