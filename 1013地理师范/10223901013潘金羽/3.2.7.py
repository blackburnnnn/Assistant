count=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            if (a!=b) and (a!=c) and (b!=c) :
                print("{}{}{}".format(a,b,c))
                count+=1
                print("共{}个".format(count))
                
