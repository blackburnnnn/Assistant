x=2
y=1
s=0
for i in range(100):
    n=int(input("请输入:"))
    if n<=0:
        print("n输入错误")
    else:
        for i in range(1,n+1):
            s=float(s+x/y)
            x,y=x+y,x
        print("前{}项的累加和为{:4.2f}".format(n,s))
    
