#百元买百鸡
for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if 3*a+2*b+c*1/3==100 and a+b+c==100:
                print('母鸡{}只，公鸡{}只，小鸡{}只'.format(a,b,c))
