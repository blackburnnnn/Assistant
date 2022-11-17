n=int(input("n="))
if n<=0:
        print("n输入错误！")
        exit(0)
s,x,t,z=0,1,1,0
for i in range(1,n+1):
     z=x+t
     x=t
     s=z/x+s
     t=z
print('前{}项的累加和为:''{:.2f}'.format(n,s))
