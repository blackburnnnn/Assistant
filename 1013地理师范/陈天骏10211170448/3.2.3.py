n = int(input())
if n<=0:
    print("n输入错误")
else:
    a,b,sum=1,1,0
    for i in range(1,n+1):
        a,b=b,b+a
        sum += b/a
    print("前{}项的累加和为{:4.2f}".format(n,sum))
