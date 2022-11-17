for i in range(1,100):
    for j in range(1,100):
        x=100-i-j
        if (3*i+2*j+x/3==100)and x%3==0:
            print('母鸡，公鸡，小鸡的数量分别为',i,j,x)
            
