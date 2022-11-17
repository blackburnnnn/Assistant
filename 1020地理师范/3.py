for i in range(1,100):
    k,n=0,0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2:
        n=n+1
        if n%5==0:
            print(i)
        else:
            print(i,"",end="")
