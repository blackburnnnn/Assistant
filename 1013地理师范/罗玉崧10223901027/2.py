s=0
t=0
k=0
for i in range(1,1001):
    s=0
    for x in range(1,i):
        if i%x==0:
            s=s+x
    if i==s:
        print(i)
        if i<100:
            t=t+1
print("100以内的完数有",t,"个")            
            
