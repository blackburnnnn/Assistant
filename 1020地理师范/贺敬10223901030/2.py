acc=[2]
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
        if j==i-1:
            acc.apppend(i)
            p=""
            q=1
            for t in acc:
                p=p+" "+str(t)
                if q%5==0 or q==len(acc):
                    print(p)
                    p=""
                    q=q+1
