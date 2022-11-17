for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if 3*a+2*b+c/3==100 and a+b+c==100:
                print('购买方案为母鸡买',a,'只，公鸡买',b,'只，小鸡买',c,'只')
