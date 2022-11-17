for x in range(100):
    for y in range(100):
        z=100-x-y
        if z%3==0 and 3*x+2*y+z//3==100:
          if x!=0 and y!=0 and z!=0:
            print(x,y,z)
