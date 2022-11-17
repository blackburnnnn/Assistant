count=0
for a in range(1,4):
    for b in range(4):
        if a!=b:
            for c in range(4):
                if a!=c and b!=c:
                    d=a*100+b*10+c
                    count+=1
                    print(f'{d}',end='\t')
                    if count%10==0:
                        print('\r')
print()
print(f'共{count}个')
                    
                
    
