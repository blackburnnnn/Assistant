x=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
             break
    else:
        print('%3.0f'%(i),end='')
        x=x+1
        if x%5==0:
            print()
        

        
