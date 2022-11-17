s=0
for a in range(2,101):
    for b in range(2,a):
        if a%b==0:
            break
    else:
        s+=1
        print(a,end=' ')
        if s%5==0:
            print( )
        
