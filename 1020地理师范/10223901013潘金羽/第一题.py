import math
total=0
s=0
for i in range(1,101):
    for j in range(1,101):
        for k in range(3,101,3):
            s=3*i+2*j+1/3*k
            total=i+j+k
            if total==100 and s==100:
                print("母鸡数{},公鸡数{}，小鸡数{}".format(i,j,k))
            
            
               
