n=0
for i in range(1,1001):
    s=0
    for b in range(1,i):
        if i%b==0:
            s+=b
    if s==i:
        print(i)
        n=n+1
print("1~1000间的完数共有",n,"个")
