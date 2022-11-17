n=int(input("n="))
if n<=0:
    print("n输入错误")
else:
    a=1
    b=1
    sum=0
    for i in range(n):
        s=a
        a=a+b
        b=s
        sum+=a/b
        print("前{}项的累加和为{:.2f}".format(n,sum))
