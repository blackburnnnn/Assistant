count=0
num=0
for i in range(1,4):
 for j in range(0,4):
  for k in range(0,4):
   if( i != k ) and (i != j) and (j != k):
    print(100*i+10*j+k,end="  ")
    count+=1
    num+=1
    if count==10:
      print("\n")
print("\n")
print('0,1,2,3可以组成',num,'个不同的三位数')
      
