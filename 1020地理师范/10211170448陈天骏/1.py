for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            if a+b+c==100 and 3*a+2*b+c/3==100:
                print("母鸡",a,"只，公鸡",b,"只，小鸡",c,"只")
