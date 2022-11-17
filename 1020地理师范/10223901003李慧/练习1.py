for x in range(1,34):
    for y in range(1,50):
       z=100-x-y
       if z%3==0 and 3*x+2*y+z//3==100:
          print("hen=",x,"cock=",y,"chicken=",z)

