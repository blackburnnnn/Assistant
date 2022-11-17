c=0
for a in range(2,101):
    for i in range(2,a):
        if a%i==0:
            break
        else:
            print(a,end='')
            c+=1
            if c%5==0:
                print()
