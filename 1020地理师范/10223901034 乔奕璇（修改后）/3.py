count=0
for n in range(2,101):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print(f'{n}\t',end='')
        count=count+1
        if count % 5 == 0:
            print(end='\n')
            
        
