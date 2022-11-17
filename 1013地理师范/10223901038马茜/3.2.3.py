n=int(input("n="))
if n<=0:
    print("n输入错误!")
    exit(0)
a=2
b=1
sum=0
for i in range(n):
    sum+=a/b
    a,b=a+b,a
print("分数数列的累加和为:{}".format(sum))
