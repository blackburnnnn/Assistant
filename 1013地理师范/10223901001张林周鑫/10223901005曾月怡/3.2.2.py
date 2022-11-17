while True:
    n=int(input("请输入n的值"))
    if n>0:
        a=1
        b=1
        sun=0
        for i in range(n):
            c=a
            b=a+b
            b=c
            sum+=a/b
        print("前{：d}项的累加和为{：4，2f}".format(n,sum))
        break
    else:
        print("n输入错误")
    
