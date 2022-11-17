list=[0,1,2,3]
n=0
for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if (list[i]!=0)and(list[i]!=list[j])and(list[j]!=list[k])and(list[i]!=list[k]):
                print('%d'%(list[i]*100+list[j]*10+list[k]),end=' ')
                n+=1
                if n==10:
                    print('\n')
print('\n')
print('共',n,'个')
