total=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print("共{}个".format(total))
