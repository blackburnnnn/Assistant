b=0
num=0
for i in range(1,1001):
  list1=[]
  for a in range (1,i):
     if i%a==0:
         list1.append(a)
  if sum(list1)==i: 
       print(i)
       num+=1
print("1~1000的完数共有",num,"个",sep="")


 
