n=100
count=0
for x in range(2,n+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        count+=1
        print(x,end=" ")
        if count%5==0:
            print()
