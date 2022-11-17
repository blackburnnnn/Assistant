n=int(input("n="))
if n<0:
    print("n输入错误!")
    exit(0)
elif n==0:
    print('阶乘和为:1')
else:
    s,t=0,1
    for i in range(1,n+1):
        t=t*i
        s=s+t
    print("阶乘和为:",s)
