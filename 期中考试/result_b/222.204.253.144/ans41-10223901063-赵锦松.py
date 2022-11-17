n=int(input("请输入行数:"))
if n%2!=0:
    for i in range(1,n+1):
        if i==1 or i==n:
            print("*"*n)
        else:
            s=int((n-1)/2)
            print(" "*s+"*"+" "*s)
else:
    n=n+1
    for i in range(1,n+1):
        if i==1 or i==n:
            print("*"*n)
        else:
            s=int((n-1)/2)
            print(" "*s+"*"+" "*s)
