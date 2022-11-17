i=1
j=1
n=0
for i in range(1,1000):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        n=n+1
        print(i)
print('1~1000内的完数共有%d个'%n)


    
            
