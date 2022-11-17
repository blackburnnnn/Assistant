count=0
for a in range(1,4):
    for b in range(4):
        for c in range(4):
            if a!=b and b!=c and c!=a:
                print(a,b,c)
                count+=1
print('共',count,'个')
