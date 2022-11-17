num=0
for i in range(4):
    for a in range(4):
        for b in range(4):
            if(i!=b and i!=0) and (i!=a) and (a!=b):
                print(i*100+a*10+b)
                num=num+1
                if num%10==0:
                   print('\n')
print('\n')
print('共%d个'%num)

               
