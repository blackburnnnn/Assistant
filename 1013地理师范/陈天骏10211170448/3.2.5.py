n=int(input("n="))
if n<0:
        print("n输入错误")
        exit(0)
s,t=1,1
for i in range(2,n+1):
            t=t*i
            s+=t
print("阶乘和为:",s)
