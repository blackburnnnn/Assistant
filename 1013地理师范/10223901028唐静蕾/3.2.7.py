n=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if(i!=k)and(i!=j)and(j!=k):
                print(i,j,k)
                n+=1
                print('共%s个'%n)
