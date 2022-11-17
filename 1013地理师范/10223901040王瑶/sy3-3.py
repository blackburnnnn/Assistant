n=int(input("n="))
if n<=0:
    print("n输入错误")
    exit(0)
s,t=0,1
for i in range(1,n+1):
    t=(1/t)+1
    s+=t
print("前{}项的累加和为:{:1.2f}".format(n,s))
