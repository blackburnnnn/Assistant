n=0
for i in range (2,101):
    count=0
    for j in range(2,i):
        if i%j==0:
            break
        else:
            count+=1
    if count>i-3:
        n+=1
        if n%5==0:
            print(i)
        else:
            print(i,end=' ')
