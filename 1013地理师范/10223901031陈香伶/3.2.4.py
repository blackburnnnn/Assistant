n=0
for i in range(1,1001):
    s=0
    for q in range(1,i):
        if i%q==0:
          s+=q
    if s==i:
     n=n+1
     print(i)
print(("1~1000中的完数一共有{}个").format(n))
    
        
