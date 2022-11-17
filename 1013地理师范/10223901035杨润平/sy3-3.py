n=int(input())
a=1
b=2
p=0
if n<=0:
    print("n输入错误")
else:
    i=0
    for i in range(0,n):
        m=b/a
        p=p+m
        a,b=b,a+b
    print("前{:d}项的累加和为{:.2f}".format(n,p))
