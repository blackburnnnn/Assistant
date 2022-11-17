for i in range(1,101):
    for j in range (1,101):
        for k in range(1,101):
            if i*3+j*2+k/3==100 and i+j+k==100:
                print('母鸡买{}只，公鸡买{}只，小鸡买{}只'.format(i,j,k))  
