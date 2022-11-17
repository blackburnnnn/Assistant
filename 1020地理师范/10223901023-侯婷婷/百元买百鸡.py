#x:母鸡；y:公鸡；z:小鸡
for x in range(1,101):
    for y in range(1,101-x):
        for z in range(1,101-x-y):
            if 3*x+2*y+z/3==100:
                print("购买母鸡、公鸡、小鸡的数量分别为",x,"、",y,"、",z,"只")
