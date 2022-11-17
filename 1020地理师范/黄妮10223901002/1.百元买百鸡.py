print('依次为母鸡，公鸡，小鸡数量')
for i in range(1,33):
    for j in range(1,50):
        k=100-i-j
        if 3*i+2*j+(1/3)*k==100:
            print(i,j,k)
