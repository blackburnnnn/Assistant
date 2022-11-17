count=0
for i in range(2,101):
    for j in range(2,i+1):
        if i%j==0:
            break
    if(i==j):
        if i>10:
            print(i,end=" ")
        else:
            print(i,end="  ")
        count+=1
        if count%5==0:
            print()
