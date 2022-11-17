x=0
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if i%j==0:
            break
    else:
        x=x+1
        if x%5==0:
            print(i)
        else:
            print(i,end=" ")
        

