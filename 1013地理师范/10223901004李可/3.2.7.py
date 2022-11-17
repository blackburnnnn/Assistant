count=0
num=0
for a in range(1,4): 
    for b in range(0,4):
        for c in range(0,4):
            if a!=b and a!=c and b!=c:
                num=100*a+10*b+1*c
                count+=1
                print(num,count)
