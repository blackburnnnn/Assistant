n=int(input("n="))
s=1
t=2
S=0
if n<=0:
    print("n输入错误!")
else:
    for i in range(0,n):
        S=S+t/s
        t=s+t
        s=t-s
print("累加和为{:.2f}".format(S))
    
    
    
    
