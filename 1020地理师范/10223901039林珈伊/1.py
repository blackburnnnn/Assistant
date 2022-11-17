for i in range(1,100):
    for j in range(1,100):
        if i*3+j*2+(100-i-j)/3==100 and (100-i-j)%3==0:
            print('母鸡买%d只，公鸡买%d只，小鸡买%d只'%(i,j,100-i-j))
        
