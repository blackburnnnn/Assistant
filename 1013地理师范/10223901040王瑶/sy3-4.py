m=0
for i in range(1,1001):
    S=0
    for n in range(1,i):
        if i%n==0:
           S+=n
    if S==i:
       m+=1
       print(i)
print("1~1000间的完数共有{}个".format(m))
