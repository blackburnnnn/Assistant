while 520<1314:
    n=int(input("请输入一个正整数n:"))
    i=1
    a=2
    b=1
    c=a+b
    S=0
    if n<=0:
        print("n输入错误")
    else:
        while i<=n:
            k=a/b
            S=S+k
            b=a
            a=c
            c=a+b
            i=i+1
    print(S)
        
        
        
