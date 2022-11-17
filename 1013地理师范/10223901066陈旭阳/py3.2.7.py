i=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            s=a*100+b*10+c            
            if a!=b and b!=c and a!=c:
                    print(s,'',end="")
                    i=i+1
print('共',i,'个')
