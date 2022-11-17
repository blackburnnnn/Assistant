x=int(input('请输入行数:'))
if x%2!=0:
   for l in range(1,x+1):
        print("*",end='')
   for i in range(1,x):
        print("   *")
   for k in range(1,x+1):
        print("*",end='')
else:
   x=x+1
   for l in range(1,x+1):
        print("*",end='')
   for i in range(1,x):
        print("   *")
   for k in range(1,x+1):
        print("*",end='')
