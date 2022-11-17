a=2
b=1
i=0
t=0
n=int(input())
if n<=0:
    print('n输入错误')
else:
    while i<n:
        f=a/b
        t+=f
        a,b=a+b,a
        i+=1
    print(f'前{n}项的累加和为{t:.2f}')
        
    
