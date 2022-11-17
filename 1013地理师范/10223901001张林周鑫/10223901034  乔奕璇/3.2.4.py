a=0
for j in range(2,1001):
    s=j
    for i in range(1,j):
        if j%i==0:
            s=s-i
    if s==0:
        print(j)
        a=a+1
print(f'1-1000间的完数共有{a}个')
        
            
            
            
