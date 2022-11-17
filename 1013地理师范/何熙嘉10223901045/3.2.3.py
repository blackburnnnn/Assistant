n=int(input())
a,b=2,1
sum=2/1
for i in range(1,n):
       a,b=a+b,a
       sum+=a/b
if n<=0:
      print("n输入错误")
else:
      print("这个数列的前n项之和为{}".format(sum))


