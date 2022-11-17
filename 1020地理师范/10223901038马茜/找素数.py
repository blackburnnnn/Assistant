c=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c+=1
        print(i,end=" ")
        if count%5==0:
            print()
