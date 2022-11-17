count=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
           if i!=j and j!=k and i!=k:
              print("{}{}{} ".format(i,j,k),end="")
              count=count+1
              if count%10==0:
                   print('\n')
print('\n')
print("共{}个".format(count))
