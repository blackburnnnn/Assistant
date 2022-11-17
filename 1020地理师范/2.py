for i in range(1,10):
    for j in range(1,10):
        if i<=j:
            s=i*j
            print("{:d}*{:d}={:d}".format(i,j,s),end=" ")
