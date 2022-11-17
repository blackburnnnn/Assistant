n=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            n+=1
            print(i,end='\t')
            if n%5==0:
                print()


