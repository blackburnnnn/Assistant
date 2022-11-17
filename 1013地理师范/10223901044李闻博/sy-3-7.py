#穷举三位数
count=0
num=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            if (a!=b)and(b!=c)and(a!=c):
                print(a*100+b*10+c,end=" ")
                count+=1
                num+=1
                if count==10:
                    print("\n")
print("\n")
print('0,1,2,3可以组成',num,'个不同的三位数')
        
                
