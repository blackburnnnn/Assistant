n=int(input("n="))
s,t=0,1
if n<0:
    print("n输入错误")
    exit(0)

elif n==0:
    print("阶乘和为1")
else:    
    for i in range(1,n+1):
        t=t*i
        s=s+t
    print("阶乘和为",s)    
