for a in range (1,100):
    for b in range(1,100):
        c=100-a-b
        if 3*a+2*b+(1/3)*c==100:
            print("母鸡",a,"只","公鸡",b,"只","小鸡",c,"只")
