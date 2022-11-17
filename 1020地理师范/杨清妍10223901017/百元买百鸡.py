print("购买方案有：")
for x in range(1,101):
    X=x*3
    for y in range(1,101):
        Y=y*2
        for z in range(1,101):
             Z=z*1/3
             if X+Y+Z==100 and x+y+z==100:
                    print("买母鸡{}只，买公鸡{}只，买小鸡{}只".format(x,y,z))

        
