count=0
num=0
for i in range(1,4):
 for j in range(0,4):
  for k in range(0,4):
   if i!=j and j!=k and k!=i:
    print(100*i+10*j+1*k)
    count+=1
    num+=1
    if count==10:
       print("\n")
print("\n")
print(f'共{num}个')









