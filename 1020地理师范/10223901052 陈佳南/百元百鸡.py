for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if a*2+b*3+c/3==100 and a+b+c==100:
                print("母鸡",b,"只","公鸡",a,"只","小鸡",c,"只")
