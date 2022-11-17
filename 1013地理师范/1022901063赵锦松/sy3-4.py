s=0
for i in range(1001):
    for j in range(1,int(i/2)+2):
        if i%j==0:
            s=s+j
    if s==i:
        print(s)
    s=0
    
