count=0
for i in range(1,1001):
    n=[]
    for j in(range(1,i)):
        if i%j==0:
            n.append(j)
    if sum(n)==i:
       count +=1
       print(i)
print('1—1000间的完数共有%d个'%count)
