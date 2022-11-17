count=0
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            if i!=j and j!=k and k!=i and i!=0:
               count+=i
               print(i,j,k)
s=count/2
print("共有",s,"个")
