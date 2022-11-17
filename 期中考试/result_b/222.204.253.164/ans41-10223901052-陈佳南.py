x=int(input("请输入行数："))
if x%2!=0:
    for i in range (1,x+1):#行数
        if i==1 or i==x:
                print("*"*x)
        else:
            for j in range(1,x+1):#每行位置
                if j!=(x+1)/2:
                    print(" ",end="")
                else:
                    print("*")
else:
    x=x+1
    for i in range (1,x+1):#行数
        if i==1 or i==x:
                print("*"*x)
        else:
            for j in range(1,x+1):#每行位置
                if j!=(x+1)/2:
                    print(" ",end="")
                else:
                    print("*")
                    
       
