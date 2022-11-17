for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            if (3*a+2*b+c/3)==100 and a+b+c==100:
                print(f'可以买母鸡{a}只，公鸡{b}只，小鸡{c}只')
