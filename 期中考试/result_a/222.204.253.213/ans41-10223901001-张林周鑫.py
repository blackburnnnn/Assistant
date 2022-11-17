x=int(input('请输入行数：'))
if x%2==0:
    x=x+1
i=1
k=""
g=""
p=""
while i<= x*2-1:
    if i==1:
        for j in range(1,x+1):
            k=k+"*"
        print(k)
    elif i<x*2-1 and i%2==1:
        for j in range(1,x+1):
            if j< x//2+1:
                p=p+" "
            elif j== x//2+1:
                p=p+"*"
            else:
                p=p+" "
        print(p)
        p=""
                
    elif i<x*2-1 and i%2==0:
        print("")
    else:
        print(k)
    i=i+1
        
