x=0
i=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
           if a!=b and b!=c and a!=c:
            print(100*a+10*b+c,end=" ")
            x+=1
            i+=1
            if i==10:
                 print("\n")
print("\n")
print("共",x,"个")
