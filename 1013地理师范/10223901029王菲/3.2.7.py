#sy3-7
count=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if i!=j and k!=i and k!=j:
                print(i,j,k,end="     ")
                count+=1
                if count%10==0:
                  print("\n")
print("\n")
print('共',count,'个')
                
