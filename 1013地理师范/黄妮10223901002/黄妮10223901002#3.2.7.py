n=0
b=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if (i!=j)and(i!=k)and(j!=k):
                n+=1
                b+=1
                print(100*i+10*j+k,end=" ")
                if b==10:
                    print("\n")
print("\n")
print('0,1,2,3可以组成',n,'个不同的三位数')
                
