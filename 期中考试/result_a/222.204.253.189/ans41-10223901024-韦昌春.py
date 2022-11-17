a=int(input("请输入行数："))
n=(a+1)/2
for i in range(1,a+1):
    if i==1 or i==a:
        print(a*"*")
    else:
        print("*")
