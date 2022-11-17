count=0
for x in range(1,4):
    for y in range(0,4):
        for z in range(0,4):
            if x!=y and y!=z and x!=z:
                print("%d%d%d"%(x,y,z),end=' ')
                count+=1
                if count%10==0:
                    print('\n')
print('\n')
print("共{}个".format(count))


