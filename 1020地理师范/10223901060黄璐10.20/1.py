for a in range(1,100):
 for b in range(1,100):
  for c in range(1,100):
    if a+b+c==100 and 3*a+2*b+1/3*c==100:
        print('母鸡{},公鸡{},小鸡{}'.format(a,b,c))
