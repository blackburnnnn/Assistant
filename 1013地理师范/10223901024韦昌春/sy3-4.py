#找出1000之内的所有的完数，并输出出该完数，统计1000之内一共有多少个完数。
n=0
for i in range(1,1001):
    a=0
    for j in range(1,i):
        if i%j==0:
            a+=j
    if a==i:
        print(i)
        n+=1
print("1~1000间的完数共有",n,"个")     
