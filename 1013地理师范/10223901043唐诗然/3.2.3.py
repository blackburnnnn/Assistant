n=int(input("n="))
if n<=0:
    print("n输入错误")
    exit(0)
else:
    total=0
    a,b=2,1
    for i in range(n):
        total=total+a/b
        a=a+b
        b=a-b
    print(total)
