for i in range(1,1001):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
print("1-1000之间的完数有3个")
        
    
