n=0
for i in range(1,1001):
    x=[]
    for j in range(1,i):
        if i%j==0:
            x.append(j)
    if sum(x)==i:
            print(i)
            n +=1
print('1~1000间的完数总共有',n,'个')
