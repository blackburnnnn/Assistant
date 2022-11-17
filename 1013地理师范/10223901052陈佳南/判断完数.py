n=0
for i in range(1,1001):
    m=0
    a=1
    while a<i:
        if i%a==0:
           m=m+a
        a=a+1
    if m==i:
       print(i)
       n=n+1
print("1-1000间的完数共有",n,"个")
