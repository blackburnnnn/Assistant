n=int(input(""))
a=1
b=1
t=0
s=0
if n>0:
    for i in range(1,n+1):
        t=b
        b=a+b
        a=t
        s=s+b/a
    print(f'前{n}项的累加和为{s:3.2f}')
else:
    print('n输入错误')
    
