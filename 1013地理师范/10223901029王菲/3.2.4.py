#程序sy3-4.py
for i in range(1,1001):
    sum=0
    for x in range(1,i):
        if i%x==0:
            sum+=x
    if sum==i:
              print(i)
m=0
for j in range(1,101):
    sum=0
    for x in range(1,j):
        if j%x==0:
         sum+=x
    if sum==j:
             m+=1
print('1~100间的完数共有',m,'个')
    
