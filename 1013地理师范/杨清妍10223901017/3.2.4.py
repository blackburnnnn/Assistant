c=0
for i in range(1,1001):
    s=0
    for a in range(1,i):
        b=i % a
        if b==0:
            s += a
    if s==i:
               c=c+1
               print(i)
print("1~1000之间的完数有{}个".format(c))

    
