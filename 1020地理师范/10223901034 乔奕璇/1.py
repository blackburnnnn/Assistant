for a in range(1,99):
    for b in range(1,99):
        for c in range(1,99):
            if a+b+c==100 and 3*a+2*b+1/3*c==100:
                print(f'买母鸡{a}只,公鸡{b}只,小鸡{c}只')
