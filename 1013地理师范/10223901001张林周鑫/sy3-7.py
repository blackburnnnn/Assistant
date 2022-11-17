arr=[]
for a in range(1,4):
    for b in range(4):
        for c in range(4):
            if a!=b and b!=c and c!=a:
                k=a*100+b*10+c
                arr.append(k)
q=""
t=1
length=len(arr)
for i in arr:
    q=q+" "+str(i)
    if t%10==0 or t==length:
        print(q)
        q=""
    t=t+1
            
