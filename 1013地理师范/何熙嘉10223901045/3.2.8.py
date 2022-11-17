n=int(input('请输入一个正整数：'))
while n!=1:
 if n<0:
  print('请重新输入')
 else:
  if n==1:
   print('1')
  else:
   if n%2==0:
    n=n/2
    print(n)
   else:
    n=3*n+1
    print(n)









