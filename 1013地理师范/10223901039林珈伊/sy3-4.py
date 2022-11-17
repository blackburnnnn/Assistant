a=0
for i in range(1,1001):
    s=0
    for n in range(1,i):
        if i % n == 0:
            s+=n
    if s == i:
       a=a+1
       print(i)
print('1~1000间的完数共有',a)
        
