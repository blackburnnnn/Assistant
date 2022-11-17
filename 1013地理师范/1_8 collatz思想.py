n=int(input("n="))
if n<0:
    print("n输入错误")
while not n==1:
    if n%2==0:
           n=n/2
    else:
         n=3*n+1
    print(n)
