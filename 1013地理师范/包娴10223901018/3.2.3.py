n=int(input())
a,b,s=2,1,0
if n<=0:
   print("n输入错误")
else:
 for i in range(1,n+1):
    s+=a/b
    a,b=a+b,a
 print("前{:n}项的和为{:.2f}".format(n,s))

n=int(input())
a,b,s=2,1,0
if n<=0:
   print("n输入错误")
else:
 for i in range(1,n+1):
    s+=a/b
    a,b=a+b,a
 print("前{:n}项的和为{:.2f}".format(n,s))
