n=int(input("请输入n的值"))
a=1
b=2
s=0
if n<=0:
    print("n输入错误")
else:
    for i in range(n):
     x=b/a
     s+=x
     a,b=b,a+b
print("前{:d}项的累加和为{:4.2f}".format(n,s))
