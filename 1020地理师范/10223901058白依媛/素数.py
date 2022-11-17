c=0
for a in range(2,101):
    for b in range(2,a):
        if a%b==0:
           break
    else:
            c+=1
            print(a,end="")
            if c%5==0:
                print()
