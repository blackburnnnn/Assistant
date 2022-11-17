for j in range(1,10):
    for i in range(1,j+1):
        x=j*i
        print('%3.1f*%3.1f=%4.1f  '%(j,i,x),end='')
    print()
