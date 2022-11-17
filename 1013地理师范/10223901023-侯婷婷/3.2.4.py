#1~1000之间的完数
n=0
for i in range(1,1001):
    list1=[]
    for a in range(1,i):
        if i%a==0:
            list1.append(a)
    if sum(list1)==i:
        print(i)
        n+=1
    print('1~1000间的完数共有',n,'个',sep='')
