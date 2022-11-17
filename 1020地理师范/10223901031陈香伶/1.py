for a in range (1,101):
    for b in range(1,101):
        for c in range(1,101):
            if (a+b+c==100 and a*3+b*2+c/3==100):
                print('母鸡',a,'公鸡',b,'小鸡',c)
