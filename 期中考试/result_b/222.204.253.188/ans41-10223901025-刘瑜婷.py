a=int(input("请输入行数:"))
if a%2==0:
    a=a+1
for i in range(1,a+1):
    if i==1 or i==a:
        for j in range(1,a+1):
            print("*",end='')
    else:
        for k in range(1,a+1):
            if k!=(a+1)/2:
                print(" ",end='')
            else:
                print("*")
    print()

    
