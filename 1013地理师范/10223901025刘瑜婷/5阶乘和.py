n=int(input("n="))
if n<0:
    print("n输入错误")
    exit(O)
s,t=1,1
for i in range(1,n):
    t=t*(i+1)
    s=s+t
print("阶乘和为：",s)
