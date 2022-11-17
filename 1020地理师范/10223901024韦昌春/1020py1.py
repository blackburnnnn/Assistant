for x in range(1,33):
    for y in range(1,50):
        z=100-x-y
        if z%3==0 and 3*x+2*y+z//3==100:
            print("母鸡{}只，公鸡{}只，小鸡{}只。".format(x,y,z))
    
