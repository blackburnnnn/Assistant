n,count=0,0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            if a!=b and b!=c and a!=c:
                s=a*100+b*10+c
                n+=1
                print(s, end=' ')
                count += 1
                if n% 10 == 0: 
                    print(end='\n')
print(end='\n')
print("共",n,"个")
