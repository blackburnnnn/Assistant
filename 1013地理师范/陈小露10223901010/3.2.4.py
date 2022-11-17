a=0
for i in range(1,1001):
  n=1
  b=0
  while n<i:
    if i%n==0:
       b=b+n
       n=n+1
    else:
       n=n+1
  if i==b:
     print(i)
     a=a+1
print("1000以内的完数共有",a,"个")
            

