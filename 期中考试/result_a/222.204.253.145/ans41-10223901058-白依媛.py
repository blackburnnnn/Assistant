a=int(input("请输入行数："))
for i in range(1,a+1):
    if i==1 or i==a:
        b=str('*'*a)
        print(b)
    else:
     c=a//2
        d=str(''*c)
        print(d,'*')
    
