a,b,total=0,1,0
n=int(input())
for i in range(1,n+1):
    n=int(input())
    if n>0:
        a+=i
        b+=i
        total=total+b/a
        print("前{}项的累加和为{:.2f}".format(n,total))
    else:
        print("n输入错误")
        
        
