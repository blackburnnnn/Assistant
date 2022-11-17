import math
n=int(input("n="))
if n<0:
        print("n输入错误！")
        exit(0)
s,t=0,0
for i in range(1,n+1):
        t=math.factorial(i)
        s=s+t
print("阶乘和为：",s)
