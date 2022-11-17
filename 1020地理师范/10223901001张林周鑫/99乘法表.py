t=""
for a in range(1,10):
    for b in range(1,a+1):
        a=float(a)
        b=float(b)
        c=a*b
        k=str(a)+"*"+str(b)+"="+str(c)
        t=t+" "+k
        if a==b:
            print(t)
            t=""
        
        
