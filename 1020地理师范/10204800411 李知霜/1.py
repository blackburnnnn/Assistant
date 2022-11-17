for rooster in range(101):
    for hen in range(101):
        for chick in range(101):
            if rooster + hen + chick == 100 and rooster*5 + hen*3 + chick/3 == 100:
                print('公鸡{}只，母鸡{}只，小鸡{}只'.format(rooster,hen,chick))
