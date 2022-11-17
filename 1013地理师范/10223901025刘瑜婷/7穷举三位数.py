s=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if i!=j and j!=k and k!=i:
                numA=i*100+j*10+k
                print(numA)
                s=s+1

print("共",s)
