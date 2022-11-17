total=100
S=100
for a in range(1,34):
    for b in range(1,51):
        for c in range(1,301):
            if a+b+c==100 and a!=0 and b!=0 and c!=0 and 3*a+2*b+c/3==100:
                print("母鸡{:d}只,公鸡{:d}只,小鸡{:d}只".format(a,b,c))
                
