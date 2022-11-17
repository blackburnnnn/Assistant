for x in range(1,34):
    for y in range(1,51):
        z=100-x-y
        if 3*x+2*y+z/3==100:
          print("母鸡：{} 公鸡：{} 小鸡：{}".format(x,y,z))
