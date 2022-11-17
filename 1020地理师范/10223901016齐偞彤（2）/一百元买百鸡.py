for a in range(1,34):
    for b in range(1,51):
        cost=3*a+b*2+(100-a-b)/3
        if cost==100:
            print('购买方案为母鸡',a,'公鸡',b,'小鸡',100-a-b,'单位（只）')
