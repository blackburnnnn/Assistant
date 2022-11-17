count,x=0,1
for a in range(1,1001):
    for b in range(1,a):
        if a%b==0:
            x+=b
            if x==a:
                x=a
                count+=1
            else:
                break
            print("{}".format(a))
            print("1~1000间的完数共有{}个".format(count))
