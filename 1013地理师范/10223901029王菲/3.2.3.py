#sy3-3.py,3.2.3 求分数序列的和
n=int(input())
a=2
b=1
s=0
for i in range(n):
 s+=a/b
 a,b=a+b,a
if n<=0:
 print("n输入错误")
else:
 print("前{}项的累加和为{:0.2f}".format(n,s))
