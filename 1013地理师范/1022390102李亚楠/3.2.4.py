j=int(input('j='))
for i in range(1,1001):
    s=0
    for j in range(1,j):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
            
