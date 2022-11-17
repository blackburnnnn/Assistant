n=int(input(""))
if n<0:
        print("n输入错误")
else:
    a=2 
    b=1
    t=0
    for i in range(1,n+1):
        t+=a/b
        a,b=a+b,a
    print("前",n,"项的累加和为：{:.2f}".format(t))
