n=0
for i in range (1001):
    lst=[]
    for a in range(1,i):
        if i%a==0:
            lst.append(a)
    if i==sum(lst) and i!=0:
        print(i)
        n=n+1
print('1~1000间的完数共有',n,'个')
