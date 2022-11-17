count=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            if a!=b and a!=c and b!=c:
                print(f'{a}{b}{c}')
                count=count+1
                if count%10==0:
                    print(end='\n')
print(f'共{count}个')


                
                
                
