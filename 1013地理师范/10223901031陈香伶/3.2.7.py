count=0
for a in range(1,4):
    for b in range(0,4):
        for c in range(0,4):
            if(a!=b and b!=c and a!=c):
                print("%d%d%d"%(a,b,c),end=" ")
                count+=1
                if(count%10==0):
                      print(end ="\n")
print("\n")                      
print("共有%d个"%count)
                      

         

        
            
