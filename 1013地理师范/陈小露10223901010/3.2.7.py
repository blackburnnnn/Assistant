s=0
for a in range(1,4):
    for b in range(4):
        for c in range(4):
            if (a!=b) and (a!=c) and (b!=c):
                print(a*100+b*10+c)
                s=s+1
print(f'共{s}个',end'10')
        
