for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if a/3+b*3+c*2==100 and a+b+c==100:
                print('小鸡{}只,母鸡{}只,公鸡{}只'.format(a,b,c))
