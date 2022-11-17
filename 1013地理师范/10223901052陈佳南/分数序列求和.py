a=2
b=3
c=3
d=5
m=2
n=int(input("请输入n的值"))
if n<=0:
    print("n输入错误")
elif n==1:
    print("前1项的和为2.00")
else:
 for i in range (2,n+1):
    m=m+c/a
    a,b=b,a+b
    c,d=d,c+d
 print(f"前",n,"项的和为","%.2f"% m)

