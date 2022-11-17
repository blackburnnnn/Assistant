count=0
for a in range(2,1001):
    x=a
    for b in range(1,a):
        if a%b==0:
            x-=b
            if x==0:
                count+=1
                print("{}".format(a))
                print("1~1000间的完数共有{}个".format(count))
