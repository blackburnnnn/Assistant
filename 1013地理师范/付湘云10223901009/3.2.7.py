n=0
for a in range(1,4):
    for b in range(4):
        for c in range(4):
            if a!=b and a!=c and b!=c:
                print(a*100+b*10+c)
                n=n+1
print('共',n,'个')
