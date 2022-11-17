count=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if(i!=k)and(j!=k)and(i!=j):
                count+=1
                m=i*100+j*10+k
                print(m,end='\t')
                if(count%10==0):
                     print("\r")
print('\n',"共{}个".format(count))
