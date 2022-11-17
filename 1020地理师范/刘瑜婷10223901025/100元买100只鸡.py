S,Q=100,100
for i in range(1,99):
    for j in range(1,99):
        k=S-i-j
        if k>0:
            if 3*i+2*j+k/3==Q:
                print("母鸡",i,"公鸡",j,"小鸡",k)
               
       
