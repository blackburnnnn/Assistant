i=0
j=0
for a in range (1,4):
 for b in range (0,4):
  for c in range (0,4):
    if (a!=b) and (a!=c) and (b!=c):
     m=a*100+b*10+c
     print(m,end=" ")
     i=i+1
     j=j+1
     if j==10:
         print('')
print('')
print("0,1,2,3可以组成",i,"个不同的三位数")

