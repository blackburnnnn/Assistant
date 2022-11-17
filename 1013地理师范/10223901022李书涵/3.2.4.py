n=0
for x in range(1,1000):
    y=0
    for i in range(1,x):
        if x % i ==0:
            y+=i
    if y == x:
         print(x)
         n+=1
print('1~1000间的完数共有%d个'%(n))
         


