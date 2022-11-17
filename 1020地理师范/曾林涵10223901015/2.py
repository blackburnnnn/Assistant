for x in range(1,50):
    for y in range(1,33):
        z=100-x-y
        if 2*x + 3*y + z/3 == 100 and z % 3==0:
            print('公鸡 %d 只 母鸡 %d 只 小鸡 %d 只'%(x,y,z))
