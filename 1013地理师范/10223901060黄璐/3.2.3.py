n=int(input("n="))
s=2
x=2
y=1
if n<=0:
     print("n输入错误")
     exit(0)
else:
    for i in range(1,n):
     x,y=x+y,x
     t=x/y
     s=s+t
print('前%1.0f项的累加和为%4.2f'%(n,s))

    
