for a in range(1,100):
    for b in range(1,100):
        if 3*a+2*b+(100-a-b)/3==100:
            print("母鸡数量为{}，公鸡数量为{}，小鸡数量为{}。".format(a,b,100-a-b))
