for m in range(1,101):
    for g in range(1,101):
        for x in range(1,101):
            if m+g+x==100 and m*3+g*2+x*(1/3)==100:
                print("母鸡",m,"只，公鸡",g,"只，小鸡",x,"只")
