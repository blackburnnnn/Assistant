for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if 3*i+2*j+1/3*k==100 and i>0 and j>0 and k>0 and i+j+k==100:
                print('母鸡{}只，公鸡{}只，小鸡{}只'.format(i,j,k))
                
                
