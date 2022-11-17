count=0
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            if(i!=k)and(i!=j)and(j!=k)and(i!=0):
                n=100*i+10*j+k
                count+=1
                print(n,end=" ")
                if count%10==0:
                    print('\n')
print('\n')
print("共{}个".format(count))
